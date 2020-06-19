from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdatedForm, ProfileUpdatedForm


def register(request):
    """ Register view"""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account has been successfully created for {username}"
            )
            return redirect("login")
    else:
        form = UserRegisterForm

    return render(request, "users/register.html", {"form": form, "title": "Register"})


@login_required
def account(request):
    """ Account view """
    if request.method == "POST":
        u_form = UserUpdatedForm(request.POST, instance=request.user)
        p_form = ProfileUpdatedForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            print(p_form)
            p_form.save()
            messages.success(request, "Account has been successfully updated")
            return redirect("account")
    else:
        u_form = UserUpdatedForm(instance=request.user)
        p_form = ProfileUpdatedForm(instance=request.user.profile)
        context = {
            "u_form": u_form,
            "p_form": p_form,
        }
        return render(request, "users/account.html", context)

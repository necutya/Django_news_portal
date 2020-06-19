from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        """ If users is created use signals """
        import users.signals

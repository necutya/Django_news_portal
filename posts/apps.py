from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = "posts"

    def ready(self):
        """Start timer"""
        import posts.updater as updater

        updater.start()

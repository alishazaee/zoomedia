from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zoomedia.blog'

    def ready(self) -> None:
        import zoomedia.blog.signals.delete_follower
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zoomediablog'

    def ready(self) -> None:
        import blog.signals.delete_follower
from django.apps import AppConfig


class AdminFormConfig(AppConfig):
    name = 'admin_form'

    def ready(self):
        import admin_form.signals

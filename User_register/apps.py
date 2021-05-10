from django.apps import AppConfig


class UserRegisterConfig(AppConfig):
    name = 'User_register'

    def ready(self):
        import User_register.signals

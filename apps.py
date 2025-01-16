from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
class MyAppConfig(AppConfig):
    name = 'myapp'
    label = 'channels'

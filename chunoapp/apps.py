from django.apps import AppConfig


class ChunoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chunoapp'

    def ready(self):
    	import chunoapp.signals

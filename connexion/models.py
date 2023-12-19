#ce class permet de gerer  les information de connexion sue django

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Client(AbstractUser):
    pass
#maintenant on indique a django son utilisation en allant 
#dans setting et gerer les autentification ligne --> 131
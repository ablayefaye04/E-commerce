from django.utils import timezone
from django.db import models
from django.urls import reverse  
from mysite.settings import AUTH_USER_MODEL



# Create your models here.
class Produit(models.Model):
    nom = models.CharField(verbose_name="Nom Produit", max_length=(20))
    prix = models.IntegerField(default=0.0)
    slug = models.SlugField(max_length=128)
    description = models.TextField(verbose_name="description")
    quantite = models.IntegerField(default=0)
    image= models.ImageField(upload_to="media", blank=True , null=True)
    
    def __str__(self):
        return self.nom #permet de retourner le nom
    def get_absolute_url(self): #sa parametre permet de lieer la page d'acceil a l'espace admin
        return reverse("produit", kwargs={"slug": self.slug})
    

    #Article:
    """"
    -Utilisateur
    -Prpduit
    -Quantite
    -commendé ou non
    """

class article(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE) #sa permet d'avoir plusier Article 
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
     #Par defaut on a pas de panier
    panier_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.nom} ({self.quantity})"

    #Panier utiliisateur(cart)
    """
    -Utilisateur
    -Arctiles
    -statut(commander ou non)
    -Date de la commande
    """
class panier(models.Model):

    Utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE) #un utilisateur ne peut avoir un et un seule panier
    #on_delete=models.CASCADE --> permet de supprimer le panier
    Articles = models.ManyToManyField(article)
    #ManyToManyField : --> parsk on a peut avoir plusieur article dans e meme panier
   
   

    def __str__(self):
        return self.Utilisateur.username

    def delete(self, *args, **kwargs):
        for article in self.Articles.all():
            article.ordered = True
            article.panier_date  = timezone.now()
            article.save()

        self.Articles.clear()
        super().delete(*args,**kwargs)
from django.contrib import admin
from django.urls import path
from bools.views import index, produit_detail,ajouter_panier,cart , delete_cart , produits, contact , service , achat
from django.conf import settings
from django.conf.urls.static import static
from connexion.views import signup , logout_user , login_user 

urlpatterns = [
    path('',index , name='index'),
    path("admin/", admin.site.urls),
    path("connexion/", signup, name="signup"), 
    path("produits/", produits, name="produits"), 
    path("Deconnexion/", logout_user, name="logout"), 
    path("cart/", cart, name="cart"), 
    path("contact/", contact, name="contact"), 
     path("payement/", achat, name="payement"), 
    path("service/", service, name="service"), 
    path("cart/delete/", delete_cart, name="delete_cart"), 
    path("Connection/", login_user, name="connection"), 
    path("produit/<str:slug>/", produit_detail, name="produit"),  
    path("produit/<str:slug>/ajouter_panier/", ajouter_panier, name="ajouter_panier"),   
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


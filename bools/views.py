from django.shortcuts import redirect, render , get_object_or_404
from django.urls import reverse
from bools.models import Produit ,panier,article

def index(request):
    produits = Produit.objects.all()
    return render(request, "bools/index.html" , context={"produits": produits})

def produits(request):
    produits = Produit.objects.all()
    return render(request, "produits.html" , context={"produits": produits})

def produit_detail(request, slug):
    produit= get_object_or_404(Produit, slug=slug)
    return render(request, 'bools/detail.html' , context={"produit": produit})

def ajouter_panier(request, slug):
    User = request.user #recuperation de l'utilisateur
    produit=get_object_or_404(Produit, slug=slug) #recuperation du produit s'il existe
    #Panier, _ =panier.objects.get_or_create(user=user) #recuperation du panier utlilisteur , si l'utilisteur n'as pas de panier donc on cree un panier
    cart, _ = panier.objects.get_or_create(Utilisateur=User)
    item,created =article.objects.get_or_create(user=User,
                                                ordered =False,
                                                product=produit) 

    if created:
        cart.Articles.add(item) #si le produit n'exuiste pas dans le panier on creeer 
        cart.save() #la on sauvegarde le produit dans le panier
    else:
        item.quantity+=1 #si le prodit existe on le l'increment
        item.save()
    return redirect(reverse("produit",kwargs={"slug":slug}))

def cart(request):
    cart=get_object_or_404(panier, Utilisateur=request.user)
    return render(request, 'bools/cart.html',context={"Articles":cart.Articles.all()})

def delete_cart(request):
    if panier:= request.user.panier:
        panier.delete()
    return redirect('index')

def contact(request):
    return render(request, "bools/contact.html" , context={"produits": produits})

def service(request):
    return render(request, "bools/service.html" , context={"produits": produits})

def achat(request):
    return render(request, "bools/payement.html" , context={"produits": produits})

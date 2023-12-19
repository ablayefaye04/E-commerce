from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model , login,logout , authenticate

# Create your views here.
User =get_user_model() #creation de l'utilisateur
def signup(request):
    
    if  request.method == "POST":
        id = request.POST.get("identifiant")  #recupertion des information de connexion
        pswd = request.POST.get("password")
        utilisateur= User.objects.create_user(username= id,password=pswd) #creation des variable de connexion avec des hash
        login(request,utilisateur)  #la connectionn
        return redirect('index') #avec la redirection de ma page index
    return render(request, 'connexion/connexion.html')   
def login_user(request):
   if request.method == "POST": #si la requette est de type POST  on connect l'utilisateur
    nom=request.POST.get("identifiant")
    pswrd=request.POST.get("password")
    user = authenticate(username=nom ,password=pswrd)
    if user:
       login(request,user)
       return redirect('index')
   return render(request, 'connexion/login.html') 
    

def logout_user(request):
    logout(request)
    return redirect('index')
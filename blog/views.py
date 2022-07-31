from multiprocessing import context
from django.shortcuts import render
from .forms import BlogForms, CardForms
from .models import CardModel

# Create your views here.

def home(request):
    card = CardModel.objects.all()
    context = {'cards':card}
    return render(request, "blog/Acceuil.html", context)

def service(request):
    
    return render(request, "blog/service.html")


def contacte(request):
    #if request.method == "POST":
    form = BlogForms(request.POST or None)
    if form.is_valid():
        form.save()
        message = "Votre message à été envoyer avec succès"
    else:
        return render(request, "blog/contacte.html", {'form':form})
    form = BlogForms()
    return render(request, "blog/contacte.html", {'form':form, 'message':message})
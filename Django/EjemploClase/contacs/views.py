from django.shortcuts import render, HttpResponse, redirect
from contacs.models import Contact

# Create your views here.
def hola(request):
    return HttpResponse('Hola esto es la clase de poo')

def index(request):
    return render(request, 'index.html')

def list(request):
    contacts = Contact.objects.all()
    return render(request, 'list.html', {'contacts': contacts})

def retrieve(request, id):
    contact = Contact.objects.filter(id=id).get()
    return render(request, 'retrieve.html', {'contact': contact})

def create(request):
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Contact.objects.create(name=name, lastName=lastname, email=email, phone=phone)

        return redirect('contactlist')"""

    return render(request, 'create.html')

def store(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Contact.objects.create(name=name, lastName=lastname, email=email, phone=phone)

        return redirect('contactlist')


def edit(request, id):
    contact = Contact.objects.filter(id=id).get()
    return render(request, 'edit.html', {'contact': contact})

def update(request, id):
    contact = Contact.objects.filter(id=id).get()
    contact.name = request.POST.get('name')
    contact.lastName = request.POST.get('lastname')
    contact.email = request.POST.get('email')
    contact.phone = request.POST.get('phone')
    contact.save()

    return redirect('contactlist')

def delete(request, id):
    contact = Contact.objects.filter(id=id).get()
    contact.delete()
    return redirect('contactlist')

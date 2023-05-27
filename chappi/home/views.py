from django.shortcuts import render,redirect
from .models import Contact,Category,Product


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        message = Contact(name=name, email=email, content=content)
        message.save()
        return redirect('index')  # Redirect back to the index page after saving the message

    return render(request, 'index.html')

def gallary(request):
    return render(request,'gallary.html')


def cooldrinks(request,c_name=None):
    # if request.method == 'GET':
    categories=None
    product=None
    if c_name!=None:
        categories=Category
        product=Product.objects.filter(category=categories)
    return render(request,'cooldrinks.html')



def hotdrinks(request):
    return render(request,'hotdrinks.html')
def snacks(request):
    return render(request,'snacks.html')



from django.shortcuts import render
from .models import Destination

# Create your views here.

def index (request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The sweetest youghurt'
    # dest1.price = '200'
    # dest1.img = 'yoghurt_1.png'
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Strawberry'
    # dest2.desc = 'The flavored youghurt'
    # dest2.price = '300'
    # dest2.img = 'yoghurt_2.png'
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = 'Strawberry'
    # dest3.desc = 'The sweetest youghurt'
    # dest3.price = '200'
    # dest3.img = 'yoghurt_3.png'
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()



    # return render(request, 'freeze/index.html', {'price': 700})
   
    # passing each object individually
    # return render(request, "freeze/index.html", {'dest1':dest1, 'dest2':dest2, 'dest3':dest3})
   
    # passing as only one object 
    return render(request, "freeze/index.html", {'dests': dests})
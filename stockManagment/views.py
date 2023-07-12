from django.shortcuts import render

# Create your views here.
def incomingItems(request):
    return render(request,'incomingItems.html')

def outcomingItems(request):
    return render(request,'outcomingItems.html')

def stockTaking(request):
    return render(request,'stockTaking.html')
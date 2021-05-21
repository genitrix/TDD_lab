from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    # items = Item.objects.all()
    return render(request, 'home.html')
    # return HttpResponse('<html><title>To-Do lists</title></html>')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')

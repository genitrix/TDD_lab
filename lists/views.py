from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request, 'home.html',{
        'new-item_text': request.POST.get('item_text',''),
    })
    # return HttpResponse('<html><title>To-Do lists</title></html>')

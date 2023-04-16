from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect


def scrape(request):
    if request.method == 'POST':
        link = request.POST.get('site','')
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
    
    
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.text
            Link.objects.create(address=link_address,name=link_text)
            return HttpResponseRedirect('/')
    else:        
        data = Link.objects.all()
        
    return render(request, 'scrape/result.html', {'data': data})

def delete(request):
    Link.objects.all().delete()
    return render(request,'scrape/result.html')

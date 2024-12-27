from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def kurslar(request):
    return HttpResponse('Kurslar Listesi')

def details(request):
    return HttpResponse('Detaylar Listesi')

def programlama(request):
    return HttpResponse('Programlama Kurs Listesi')

def mobiluygulamalar(request):
    return HttpResponse('Mobil Uygulamalar Kurs Listesi')


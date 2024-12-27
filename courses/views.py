from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect, HttpResponseNotFound

data = {
    "programlama" :"programlama kategorisne ait kurslar",
    "web-gelistirme" : "web gelistirme kategorisne ait kurslar",
    "mobil" :"mobil kategorisne ait kurslar"
}

def kurslar(request):
    return HttpResponse('Kurslar Listesi')

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} Detaylar Listesi')

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound('yanlış kategori seçimi')

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id>len(category_list)):
        return HttpResponseNotFound('yanlış kategori seçimi')
    redirect_text = category_list[category_id-1]

    return HttpResponseRedirect('/kurs/kategori/' + redirect_text)


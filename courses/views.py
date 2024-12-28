from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

data = {
    "programlama" :"programlama kategorisne ait kurslar",
    "web-gelistirme" : "web gelistirme kategorisne ait kurslar",
    "mobil" :"mobil kategorisne ait kurslar"
}
def index(request):
    return render(request, 'courses/index.html')

def kurslar(request):
    list_items = ""
    category_list = list(data.keys())
    for category in category_list:
        redirect_url = reverse('courses_by_category',args=[category])
        list_items += f"<li><a href = '{redirect_url}'>{category}</a></li>"
    html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"
        
    return HttpResponse(html)

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
    category_name = category_list[category_id-1]

    redirect_url = reverse('courses_by_category',args=[category_name])

    return HttpResponseRedirect(redirect_url)


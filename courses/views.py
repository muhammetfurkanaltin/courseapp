from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from datetime import date

data = {
    "programlama" :"programlama kategorisne ait kurslar",
    "web-gelistirme" : "web gelistirme kategorisne ait kurslar",
    "mobil" :"mobil kategorisne ait kurslar"
}
db ={
    "courses":[
        {
            "title":"python",
            "description":"python kursu açıklaması",
            "imageUrl": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
            "slug":"python-kursu",
            "date": date(2022,8,8),
            "is_active":True
        },
        {
            "title":"javascript kursu",
            "description":"javascript kursu açıklaması",
            "imageUrl": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
            "slug":"javascript-kursu",
            "date": date(2022,9,9),
            "is_active":False

        },
        {
            "title":"web gelistirme kursu",
            "description":"web gelistirme kursu açıklaması",
            "imageUrl": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
            "slug":"web-gelistirme-kursu",
            "date": date(2022,10,10),
            "is_active":False
        },
    ],
    "categories":["programlama","web-gelistirme","mobil"]
        

}



def index(request):
    
    category_list = list(data.keys())

        
    return render(request, 'courses/index.html', {
        'catogories':category_list,
    })

def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} Detaylar Listesi')

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return render(request, 'courses/kurslar.html' , {
            'category':category_name,
            'category_text':category_text
        })
    except:
        return HttpResponseNotFound('yanlış kategori seçimi')

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())

    if(category_id>len(category_list)):
        return HttpResponseNotFound('yanlış kategori seçimi')
    category_name = category_list[category_id-1]

    redirect_url = reverse('courses_by_category',args=[category_name])

    return HttpResponseRedirect(redirect_url)


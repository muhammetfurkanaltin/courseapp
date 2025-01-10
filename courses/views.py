from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from datetime import date,datetime

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
            "imageUrl": "1.jpg",
            "slug":"python-kursu",
            "date": datetime.now(),
            "isActive":True,
            "isUpdated":False
        },
        {
            "title":"javascript kursu",
            "description":"javascript kursu açıklaması",
            "imageUrl": "2.jpg",
            "slug":"javascript-kursu",
            "date": date(2022,9,9),
            "isActive":True,
            "isUpdated":True

        },
        {
            "title":"web gelistirme kursu",
            "description":"web gelistirme kursu açıklaması",
            "imageUrl": "1.jpg",
            "slug":"web-gelistirme-kursu",
            "date": date(2022,10,10),
            "isActive":False,
            "isUpdated":False
        },
    ],
    "categories":[
        {"id":1,"name":"programlama", "slug":"programlama"},
        {"id":2,"name":"mobil-Gelistirme", "slug":"mobil"},
        {"id":3,"name":"web-Gelistirme", "slug":"web-gelistirme"},
        
    ]
}



def index(request):
    #list comprehension
    kurslar = [course for course in db['courses'] if course['isActive'] == True]
    
    kategoriler = db['categories']

        
    return render(request, 'courses/index.html', {
        'categories':kategoriler,
        'courses': kurslar
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


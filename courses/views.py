from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse ,HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from datetime import date,datetime
from .models import Course , Category

data = {
    "programlama" :"programlama kategorisne ait kurslar",
    "web-gelistirme" : "web gelistirme kategorisne ait kurslar",
    "mobil-uygulamalar" :"mobil kategorisne ait kurslar"
}
db ={
    "courses":[
        {
            "title":"python",
            "description":"python kursu açıklaması",
            "imagUrl": "1.jpg",
            "slug":"python-kursu",
            "date": datetime.now(),
            "isActive":True,
            "isUpdated":False
        },
        {
            "title":"javascript kursu",
            "description":"javascript kursu açıklaması",
            "imagUrl": "2.jpg",
            "slug":"javascript-kursu",
            "date": date(2022,9,9),
            "isActive":True,
            "isUpdated":True

        },
        {
            "title":"web gelistirme kursu",
            "description":"web gelistirme kursu açıklaması",
            "imagUrl": "1.jpg",
            "slug":"web-gelistirme-kursu",
            "date": date(2022,10,10),
            "isActive":False,
            "isUpdated":False
        },
    ],
    "categories":[
        {"id":1,"name":"programlama", "slug":"programlama"},
        {"id":2,"name":"mobil-uygulamalar", "slug":"mobil-uygulamalar"},
        {"id":3,"name":"web-Gelistirme", "slug":"web-gelistirme"},
        
    ]
}



def index(request):
    #list comprehension
    kurslar = Course.objects.filter(isActive=1)
    
    kategoriler = Category.objects.all()

        
    return render(request, 'courses/index.html', {
        'categories':kategoriler,
        'courses': kurslar
    })

def details(request,slug):

    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'courses/details.html',context)

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


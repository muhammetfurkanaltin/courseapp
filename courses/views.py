from django.shortcuts import get_object_or_404, render , redirect
from .models import Course , Category, UploadModel
from django.core.paginator import Paginator
from .forms import CourseCreateForm, CourseEditForm, UploadForm
import os
import random

def index(request):
    #list comprehension
    kurslar = Course.objects.filter(isActive=1,isHome=1)
    
    kategoriler = Category.objects.all()

        
    return render(request, 'courses/index.html', {
        'categories':kategoriler,
        'courses': kurslar
    })

def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            # kurs = Course(
            #     title = form.cleaned_data["title"],
            #     description = form.cleaned_data["description"],   //yontem 1
            #     imagUrl = form.cleaned_data["imagUrl"],
            #     slug = form.cleaned_data["slug"]
            # )
            # kurs.save()
            form.save()          #yontem 2
            return redirect('/kurslar')
    else:
        form = CourseCreateForm()
    return render(request, 'courses/create_course.html', {'form':form})

def course_list(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/course-list.html', {'courses':kurslar})

def course_edit(request,id):
    course = get_object_or_404(Course, pk=id)
    form = CourseEditForm(instance=course)
    if request.method == "POST":
        form = CourseEditForm(request.POST, instance=course)
        form.save()
        return redirect('course_list')
    else:
        form = CourseEditForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form':form})

def course_del(request,id):
    course = get_object_or_404(Course, pk=id)
    if request.method == "POST":
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/course_del.html', )

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = UploadForm(image = request.FILES['image'])
            model.save()
            return render(request, 'courses/success.html')
    else:
        form = UploadForm()
    return render(request, 'courses/upload.html', {'form':form})


def details(request,slug):

    course = get_object_or_404(Course, slug=slug)

    return render(request, 'courses/details.html',{'course':course})

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True,title__contains=q).order_by('-id')
        kategoriler = Category.objects.all()
    else:
        return redirect('/kurslar')
    return render(request, 'courses/search.html',{
        'categories':kategoriler,
        'courses': kurslar,
        
    })
def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by('-id')
    kategoriler = Category.objects.all()
    paginator = Paginator(kurslar, 2)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)
    return render(request, 'courses/list.html',{
        'categories':kategoriler,
        'page_obj': page_obj,
        'seciliKategori':slug
    })


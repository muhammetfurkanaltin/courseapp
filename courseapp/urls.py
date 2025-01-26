
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('kurslar/', include('courses.urls')),
    path('', include('pages.urls')),
    path('account/', include('account.urls')),
    path('books/', include('book_api.urls')),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#courseapp
#courses
#pages

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings




api_patterns = [
    path('',include('myapp.urls'),),
    path('product/',include('product.urls'),),
   
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(api_patterns)),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)

print(static(settings.MEDIA_URL,document_root=settings.MEDIA_URL))


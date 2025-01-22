from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register.as_view(),name='register/'),
    path('login/',views.Loginview.as_view(),name='login/'),
    path('send-otp/',views.send_otp.as_view(),name='send-otp/'),
    path('varify-otp/',views.varify_otp.as_view(),name='varify-otp/'),
    path('reset-pass/',views.reset_password.as_view(),name='reset-pass/'),
    path('get-user/',views.getusers.as_view(),name='get-uer/'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
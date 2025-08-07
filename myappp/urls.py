from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('teaStation/',views.home, name='home'),
    path('',views.home)
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


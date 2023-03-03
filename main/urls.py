from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('blog/', views.PostList.as_view(), name='blog'),
  path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
  path('services/', views.services, name='services'),
  path('work/', views.work, name='work'),
  path('contact/', views.contact, name='contact'),
  path('send-message/', views.send_message, name='send_message')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


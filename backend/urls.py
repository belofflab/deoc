from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]


handler404='main.views.handler404'
handler500='main.views.handler500'
handler403='main.views.handler403'
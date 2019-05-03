from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html")),
    path('admin/', admin.site.urls),
    path('messages/', include('chat.urls')),
]

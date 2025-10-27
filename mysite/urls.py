from django.contrib import admin
from django.urls import path, include  # 👈 importante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # 👈 conecta el blog al dominio raíz
]


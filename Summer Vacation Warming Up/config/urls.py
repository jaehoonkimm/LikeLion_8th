"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from summer_app import views
import summer_app.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', summer_app.views.main, name="main"),
    path('detail/<int:detail_id>', summer_app.views.detail, name="detail"),
    path('create/', summer_app.views.create, name="create"),
    path('update/<int:update_id>', summer_app.views.update, name="update"),
    path('delete/<int:delete_id>', summer_app.views.delete, name="delete"),
    # path('photoForm_function/', summer_app.views.photoForm_function, name="photoForm_function")
]
urlpatterns += static(settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                     document_root=settings.MEDIA_ROOT)
"""Djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from registration import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('store/', user_views.store, name='store'),
    path('store/item/<int:pk>/', user_views.ProductDetailView, name="item-details"),
    path('store/cart', user_views.cart, name='cart'),
    path('store/checkout/', user_views.Checkout, name='checkout'),
    path('process_order/', user_views.processOrder, name='process_order'),
    path('update_item/', user_views.updateItem, name='update_item'),
    path('profile/CV', user_views.pdf_view, name='pdf'),
    path('profile/diary', user_views.diaryrequest, name='diary'),
    path('profile/diary/add',user_views.DiaryCreateView.as_view(), name = 'diary-add'),
    path('profile/diary/additem',user_views.DiaryItemCreateView.as_view(), name = 'diaryitem-add'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/<str:username>', user_views.ViewProfile, name='profile_user'),
    path('profile/upload', user_views.uploadstats, name="profile_upload"),
    path('upload/<str:stat>/<str:steps>', user_views.uploadstats, name="profile_upload"),
    path('retrieve/<str:stat>/<str:username>', user_views.retrieve, name="profile_retrieve"),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('', include('blog.urls')),
]



from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

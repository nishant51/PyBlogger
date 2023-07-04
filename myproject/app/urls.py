from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('create',views.create,name='create'),
    path('editblog/<int:pk>/', views.editblog, name='editblog'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('readmore/<int:pk>',views.readmore,name='readmore'),
    path('register',views.register,name="register"),
    path('login',views.loginpage,name="login"),
    path('logout',views.logoutpage,name='logout'),

]
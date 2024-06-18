from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='blog_post'),
    path('create/',views.create,name='create_post'),
    path('edit/<int:id>/',views.edit,name='edit_post'),
    path('delete/<int:id>/',views.delete,name='delete_post'),
]





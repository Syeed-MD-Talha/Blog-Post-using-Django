from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='blog_post'),
    path('create/',views.create,name='create_post'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



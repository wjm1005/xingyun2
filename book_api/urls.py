from django.conf.urls import url, include
from book_api import views

urlpatterns = [
    url('book_list/', views.NovelBook_list),
]
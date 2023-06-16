from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('books/',views.books,name = 'books'),
    path('update/<int:id>',views.update,name = 'update'), # url = int fro one book
    path('delete/<int:id>',views.delete,name = 'delete'),
    path('delete1/<int:id>',views.delete,name = 'd'),
    path('facse/',views.faces,name = 'faces'),

]

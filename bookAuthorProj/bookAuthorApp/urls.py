from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_add', views.process_add),
    path('books/<int:book_id>', views.books),
    path('add_author/<int:id>', views.add_author),
    path('authors', views.authors),
    path('view_author/<int:auth_id>', views.view_author)
]
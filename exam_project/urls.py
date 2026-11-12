from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home_page/', home_page, name="home_page"),
    path('add_author/', add_authors, name="add_author"),
    path('add_book/', add_books, name="add_books"),
    path('create_order/', create_order, name='create_order'),
    path('show_authors/', show_authors, name="show_authors"),
    path('show_books/', show_books, name="show_books"),
    path('show_orders/', show_orders, name="show_orders"),
    path('update_author/<int:id>/', update_authors, name="update_author"),
    path('update_book/<int:id>/', update_books, name="update_book"),
    path('update_order/<int:id>/', update_orders, name="update_order"),
    path('delete_author/<int:id>/', delete_authors, name="delete_author"),
    path('delete_book/<int:id>/', delete_books, name="delete_book"),
    path('delete_order/<int:id>/', delete_order, name="delete_order"),
    path('reg/', reg, name="reg")
]

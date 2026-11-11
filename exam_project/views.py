from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def home_page(request):
    return render(request, 'home_page.html')


def add_authors(request):
    if request.method == "POST":
        Authors.objects.create(
            name = request.POST["name"],
            age = request.POST["age"]
        )
        return redirect('home_page')
    return render(request, 'add_authors.html')


def show_authors(request):
    if request.method == "GET":
        Authors.objects.all()
    return render(request, 'show_authors.html')


def update_authors(request, id):
    author = get_object_or_404(Authors, id=id)
    if request.method == "POST":
            author.name = request.POST["name"]
            author.age = request.POST["age"]
            return redirect("home_page")
    return render(request, 'update_authors.html', {"author": author})



def delete_authors(request, id):
     author = get_object_or_404(Authors, id=id)
     if request.method == "POST":
          author.delete()
          return redirect('home_page')
     return render(request, {"author": author})



def add_books(request):
    if request.method == "POST":
        Books.objects.create(
             name = request.POST["name"],
             ganre = request.POST["gabre"],
             price = request.POST["price"],
             author = get_object_or_404(Authors, pk = request.POST["autor"]),
             caption = request.POST["caption"],
             picture = request.FILES.get('picture'),
             publisher = request.POST["publisher"]
        )
        return redirect('home_page')
    return render(request, 'add_book.html')



def show_books(request):
     if request.method == "GET":
          Books.objects.all()
          return render(request, 'show_book.html')



def update_books(request, id):
     book = get_object_or_404(Books, id=id)
     if request.method == "POST":
        book.name = request.POST["name"]
        book.ganre = request.POST["ganre"]
        book.price = request.POST["price"]
        book.author = get_object_or_404(Books, pk = request.POST["author"])
        book.caption = request.POST["caption"]
        book.picture = request.FILES.get('picture')
        book.publisher = request.POST["publisher"]
        return redirect('home_page')
     return render(request, 'update_books.html', {"bool": book})


def delete_books(request, id):
     book = get_object_or_404(Books, id=id)
     if request.method == "POST":
          book.delete()
          return redirect('home_page')
     return render(request, {"book": book})





def create_order(request):
     if request.method == "POST":
          Order.objects.create(
               book_name = get_object_or_404(Books, pk = request.POST["book_name"]),
               user_name = request.POST["user_name"],
               phone = request.POST["phone"],
               date = request.POST["date"]
               )
          return redirect('home_page')
     return render(request, 'create_order.html')




def show_orders(request):
     if request.method == "GET":
          Order.objects.all()
          return render(request, 'show_orders.html')


def update_orders(request, id):
     order = get_object_or_404(Order, id = id)
     if request.method == "POST":
          order.book_name = get_object_or_404(Books, pk = request.POST["book_name"])
          user_name = request.POST["user_name"]
          phone = request.POST["phone"]
          date = request.POST["date"]
          return redirect('home_page')
     return render(request, 'update_order.html', {"order": order})


def delete_order(request, id):
     order = get_object_or_404(Order, id = id)
     if request.method == "POST":
          order.delete()
          return redirect('home_page')
     return render(request, {"order": order})


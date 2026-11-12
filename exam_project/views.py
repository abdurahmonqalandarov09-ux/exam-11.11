from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def home_page(request):
    return render(request, 'home_page.html')


def add_authors(request):
    if request.method == "POST":
        Authors.objects.create(
            full_name = request.POST["full_name"],
            age = request.POST["age"]
        )
        return redirect('home_page')
    return render(request, 'add_authors.html')


def show_authors(request):
    author = Authors.objects.all()
    return render(request, 'show_authors.html', {"author": author})


def update_authors(request, id):
    author = get_object_or_404(Authors, id=id)
    if request.method == "POST":
            author.full_name = request.POST["full_name"]
            author.age = request.POST["age"]
            author.save()
            return redirect("home_page")
    return render(request, 'update_authors.html', {"author": author})



def delete_authors(request, id):
     author = get_object_or_404(Authors, id=id)
     if request.method == "POST":
          author.delete()
          return redirect('home_page')
     return render(request, 'delete_authors.html', {"author": author})



def add_books(request):
    if request.method == "POST":
        Books.objects.create(
             name = request.POST["name"],
             ganre = request.POST["ganre"],
             price = request.POST["price"],
             author = get_object_or_404(Authors, pk = request.POST["author"]),
             caption = request.POST["caption"],
             picture = request.FILES.get('picture'),
             publisher = request.POST["publisher"]
        )
        return redirect('home_page')
    return render(request, 'add_book.html', {"authors": Authors.objects.all()})



def show_books(request):
     book = Books.objects.all()
     return render(request, 'show_book.html', {"book": book})



def update_books(request, id):
     book = get_object_or_404(Books, id=id)
     if request.method == "POST":
        book.name = request.POST["name"]
        book.ganre = request.POST["ganre"]
        book.price = request.POST["price"]
        book.author = get_object_or_404(Authors, pk = request.POST["author"])
        book.caption = request.POST["caption"]
        book.picture = request.FILES.get('picture')
        book.publisher = request.POST["publisher"]
        book.save()
        return redirect('home_page')
     return render(request, 'update_books.html', {"book": book, "authors": Authors.objects.all()})


def delete_books(request, id):
     book = get_object_or_404(Books, id=id)
     if request.method == "POST":
          book.delete()
          return redirect('home_page')
     return render(request, 'delete_book.html', {"book": book})





def create_order(request):
     if request.method == "POST":
          Order.objects.create(
               book_name = get_object_or_404(Books, pk = request.POST["book_name"]),
               user_name = request.POST["user_name"],
               user_phone = request.POST["user_phone"]
               )
          return redirect('home_page')
     return render(request, 'create_order.html', {"books": Books.objects.all()})




def show_orders(request):
     order = Order.objects.all()
     return render(request, 'show_orders.html', {"order": order})


def update_orders(request, id):
     order = get_object_or_404(Order, id = id)
     if request.method == "POST":
          order.book_name = get_object_or_404(Books, pk = request.POST["book_name"])
          order.user_name = request.POST["user_name"]
          order.user_phone = request.POST["user_phone"]
          order.save()
          return redirect('home_page')
     return render(request, 'update_order.html', {"order": order, "books": Books.objects.all()})


def delete_order(request, id):
     order = get_object_or_404(Order, id = id)
     if request.method == "POST":
          order.delete()
          return redirect('home_page')
     return render(request, 'delete_order.html', {"order": order})

def reg(request):
     if request.method == "POST":
          Order.objects.create(
               user_name = request.POST["user_name"],
               user_phone = request.POST["user_phone"]
          )

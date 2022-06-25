from django import forms
from django.shortcuts import render,redirect
from .models import Book
from author.models import Author
from order.models import Order
from authentication.models import CustomUser
from .forms import BookFilterForm, BookForm
from django.utils import timezone



def index(request):
    books = Book.objects.all()
    return render(request, 'book/books.html', {'books': books, 'title':"All books"})


def books_by_author(request, id):
    author = Author.objects.get(id=id)
    all_books = Book.objects.all()
    valid_books = []
    for book in all_books:
        if author in list(book.authors.all()):
            valid_books.append(book)
    return render(request, 'book/books.html', {'books': valid_books})

def orders(request):
    orders = Order.objects.order_by('created_at', 'plated_end_at')
    return render(request, 'book/orders.html', {'orders': orders, 'title': 'Orders'})

def users(request):
    users = CustomUser.objects.all()
    return render(request, 'book/users.html', {'users': users, 'title': 'All users'})

def books_by_user(request, id):
    user = CustomUser.objects.get(id=id)
    orders = Order.objects.all()
    books = []
    for order in orders:
        if user == order.user:
            books.append(order.book)
    return render(request, 'book/books.html', {'books': books, 'title': 'Sorting books'})

def asc_name(request):
    books = Book.objects.order_by('name')
    return render(request, 'book/sort_books.html', {'books': books, 'title': 'Sorting books'})

def desc_name(request):
    books = Book.objects.order_by('-name')
    return render(request, 'book/sort_books.html', {'books': books, 'title': 'Sorting books'})

def asc_count(request):
    books = Book.objects.order_by('count')
    return render(request, 'book/sort_books.html', {'books': books, 'title': 'Sorting books'})

def desc_count(request):
    books = Book.objects.order_by('-count')
    return render(request, 'book/sort_books.html', {'books': books, 'title': 'Sorting books'})

def overdue_users(request):
    orders = Order.objects.all()
    users = []
    for order in orders:
        if order.end_at:
            if order.end_at > order.plated_end_at:
                users.append(order.user)
        else:
            if timezone.now() > order.plated_end_at:
                users.append(order.user)
    return render(request, 'book/users.html', {'users': users, 'title': 'Overdue users'})


def all_books_filter (request):
    books = Book.objects.all()
    form = BookFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_count']:
            books = books.filter(count__gte=form.cleaned_data['min_count'])
        if form.cleaned_data['max_count']:
            books = books.filter(count__lte=form.cleaned_data['max_count'])
        if form.cleaned_data['name']:
            books = books.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data['author']:
            books = books.filter(authors__in=form.cleaned_data['author'])

    return render (request, 'book/list_books.html',{'books':books,'form':form, 'title':'Find any book in our library'})


def book_description(request,book_pk):
    book = Book.get_by_id(book_pk)
    return render(request,'book/book_description.html',{"book": book})


def available_books(request):
    unreturn_books = []
    books =  Book.get_all()
    for book in books:
        for order in Order.get_not_returned_books():
            if book.id  == order.book.id:
                unreturn_books.append(book)
    for book in unreturn_books:
        if book.id:
            book.count -= 1
    return render (request, 'book/available_books.html',{'books':books, 'title':"Available books"})



def create_book (request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.name = request.POST['name']
            book.description = request.POST['description']
            book.count = request.POST['count']
            book.save()
            book.authors.add(request.POST['authors'])
        return redirect('books')
    else:
        form = BookForm()
    return render(request, 'book/create_book.html', {'form': form, 'title': 'Add New Book'})


def update_book(request, pk):
    book = Book.get_by_id(pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'book/create_book.html', {'form': form, 'title': 'Update Book'})


def delete_book(request, pk):
    book = Book.get_by_id(pk)
    if request.method == 'POST':
        Book.delete_by_id(pk)
        return redirect('/')
    return render(request, 'book/delete_book.html', {'book': book})
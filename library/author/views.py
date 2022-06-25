from django.shortcuts import render, redirect
from author.forms import AuthorForm
from author.models import Author


def authors(request):
    authors = Author.objects.all()
    return render(request, 'author/authors.html', {'authors': authors, 'title': 'All authors'})


def create_author (request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.name = request.POST['name']
            author.patronymic = request.POST['patronymic']
            author.surname = request.POST['surname']
            author.save()
        return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'author/create_author.html', {'form': form, 'title': 'Add New Author'})


def update_author(request, pk):
    author = Author.get_by_id(pk)
    form = AuthorForm(instance=author)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("/authors")
    return render(request, 'author/create_author.html', {'form': form, 'title': 'Update Author'})


def delete_author(request, pk):
    author = Author.get_by_id(pk)
    if request.method == 'POST':
        Author.delete_by_id(pk)
        return redirect('/authors')
    return render(request, 'author/delete_author.html', {'author': author})

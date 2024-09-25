from django.shortcuts import render, redirect
from .forms import SharedBookForm
from .models import SharedBook

# Create your views here.

def share_view(request):
    if request.method == 'POST':
        form = SharedBookForm(request.POST, request.FILES)
        if form.is_valid():
            shared_book = form.save(commit=False)
            shared_book.shared_by = request.user
            shared_book.save()
            return redirect('shared_books')  # Redirect to the list of shared books
    else:
        form = SharedBookForm()

    return render(request, 'share/share.html', {'form': form})

def shared_books_view(request):
    shared_books = SharedBook.objects.all()
    return render(request, 'share/shared_books.html', {'shared_books': shared_books})

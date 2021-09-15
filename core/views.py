from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View
from .models import Book, Category
from .forms import BookCreationModelForm


class HomePageView(View):

    template_name = 'core/homepage.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, self.template_name, context)

class BookDetailView(View):

    template_name = 'core/book_detail.html'

    def get(self, request, slug, *args, **kwargs):
        book = get_object_or_404(Book, slug=slug)
        context = {
            'book': book,
        }

        return render(request, self.template_name, context)


class BookCreationView(View):
    
    template_name = 'core/book_create.html'

    def get(self, request, *args, **kwargs):
        form = BookCreationModelForm
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = BookCreationModelForm(request.POST, request.FILES)
        if form.is_valid():
            book = Book.objects.create(
                name=form.cleaned_data['name'],
                author=form.cleaned_data['author'],
                uploaded_by=request.user,
                cover=request.FILES['cover'],
                category=form.cleaned_data['category']
            )
            return redirect(reverse('book-detail', kwargs={'slug': book.slug}))
        
        return render(request, self.template_name)


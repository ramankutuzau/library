import datetime

from django.shortcuts import render, redirect

from catalog.models import Reader

from catalog.forms import ReaderRegisterForm

from catalog.models import Book

from catalog.models import HistoryBook

from catalog.forms import BookForm


def catalog(request):
    try:
        current_reader_pk = request.session['current_reader']
    except:
        return redirect('login_reader')

    print(current_reader_pk)
    reader = Reader.objects.get(pk=current_reader_pk)
    books = Book.objects.all().order_by('-pk')
    history_books = HistoryBook.objects.all().order_by('-pk')
    books_current_user = HistoryBook.objects.filter(reader=reader, datetime_return=None).order_by('-pk')
    form = BookForm()
    context = {
        'reader': reader,
        'books': books,
        'history_books': history_books,
        'books_current_user': books_current_user,
        'form': form,
    }
    return render(request, 'catalog/index.html', context)


def create_reader(request):
    if request.method == 'POST':
        form = ReaderRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            middle_name = form.cleaned_data['middle_name']

            if Reader.objects.filter(first_name=first_name, last_name=last_name, middle_name=middle_name).exists():
                return render(request, 'error_register.html')

            reader_instance = form.save()
            request.session['current_reader'] = reader_instance.pk
            return redirect('catalog')

    return redirect('login_reader')


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('catalog')


def get_book(request):
    if request.method == 'GET':
        reader = Reader.objects.get(pk=request.session['current_reader'])
        book = Book.objects.get(pk=request.GET.get('book_pk'))
        book.in_stock = False
        book.save()
        HistoryBook.objects.create(
            book=book,
            reader=reader,
        )
        return redirect('catalog')


def return_book(request):
    if request.method == 'GET':
        history_book = HistoryBook.objects.get(pk=request.GET.get('history_book_pk'))
        history_book.book.in_stock = True
        history_book.book.save()
        history_book.datetime_return = datetime.datetime.now()
        history_book.save()
        return redirect('catalog')


def login_reader(request):
    if request.method == 'POST':
        request.session['current_reader'] = request.POST.get('reader_pk')
        return redirect('catalog')
    else:
        form = ReaderRegisterForm()

    readers = Reader.objects.all()

    context = {
        'readers': readers,
        'form': form,
    }
    return render(request, 'registration/login.html', context=context)


def logout_reader(request):
    if 'current_reader' in request.session:
        del request.session['current_reader']
    return redirect('login_reader')

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Books
# Create your views here.

class BaseView(View):

    def dispatch(self, request, *args, **kwargs):
        print(f'{request.method} - {request.body} - {request.build_absolute_uri()} - {request.headers}')
        result = super().dispatch(request, *args, **kwargs)
        print('Я код который выполнинлся после запроса')
        return result

class BooksView(BaseView):

    def get(self, request):
        # books = Books.objects.all()
        return JsonResponse({'status': 'Получить все данные'})

    def post(self, request):
        # books = Books.objects.all()
        return JsonResponse({'status': 'Создать новую запись'})

    def patch(self, request):
        # books = Books.objects.all()
        return JsonResponse({'status': 'Обновляем запись'})

    def delete(self, request):
        # books = Books.objects.all()
        return JsonResponse({'status': 'Удаляем запись'})

class BooksListView(ListView):
    model = Books
    template_name = 'app/base.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

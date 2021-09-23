import json
from authapp.models import User
from django.http import JsonResponse
from django.shortcuts import render
from secrets import token_urlsafe

# Create your views here.



def authentication(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = User.objects.filter(login=data['login'], password=data['password'])
        if user:
            token = token_urlsafe(32)
            user[0].token = token
            user[0].save()
            return JsonResponse({'status': 'Success', 'token': token}, status=200)
        return JsonResponse({'status': 'Аутентификация провалена'}, status=400)

def authorization(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = User.objects.filter(token=data['token'])
        if user:
            return JsonResponse({'status': 'Success'}, status=200)
        return JsonResponse({'status': 'Авторизация провалена'}, status=400)

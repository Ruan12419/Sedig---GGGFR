from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def check_authentication(request):
    if request.user.is_authenticated:
        print(f"{request.user} Autenticado")
        return JsonResponse({
            'isAuthenticated': True,
            'is_superuser': request.user.is_superuser,
            'is_staff': request.user.is_staff
        })
    else:
        print(f"{request.user} Não Autenticado")
        return JsonResponse({'isAuthenticated': False})


from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(request, username=data['email'], password=data['senha'])
        print(user)
        if user is not None:
            login(request, user)
            return JsonResponse({ 'mensagem': "Login realizado com sucesso!"}, status=200)
        else:
            return JsonResponse({'mensagem': 'Email ou senha inválidos'}, status=401)

    return JsonResponse({'mensagem': 'Método HTTP não permitido'}, status=405)


import json
import random
import traceback
from django.http import JsonResponse
from .models import Usuario

@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            random_number = str(random.randint(0, 999999)).zfill(6)
            random_suffix = str(random.randint(0, 999)).zfill(3)
            chave_passe = f"U{random_number}{data['estado']}-{random_suffix}"

            usuario = Usuario(
                nome_completo=data['nomeCompleto'],
                cpf=data['cpf'],
                chave_passe=chave_passe,
                email=data['email'],
                estado=data['estado'],
                cidade=data['cidade']
            )
            usuario.set_password(data['senha'])
            usuario.save()
            return JsonResponse({'mensagem': 'Usuário cadastrado com sucesso!'}, status=201)
        except Exception as e:
            traceback_str = ''.join(traceback.format_tb(e.__traceback__))
            error_message = f"{str(e)}\n{traceback_str}"
            return JsonResponse({'mensagem': error_message}, status=400)

    return JsonResponse({'mensagem': 'Método HTTP não permitido'}, status=405)


from django.contrib.auth import logout
from django.http import JsonResponse

@csrf_exempt
def logout_view(request):
    print(request)
    logout(request)
    return JsonResponse({'mensagem': 'Logout realizado com sucesso!'})



from django.contrib.auth.decorators import login_required
from sedig.models import Usuario

@login_required
def usuario_view(request):
    usuario = request.user
    cpf = usuario.cpf
    cpf_desejado = cpf[4:10]
    
    data = {
        'email': usuario.email,
        'cpf': f'xxx.{cpf_desejado}x-xx',
        'chavePasse': usuario.chave_passe,
        'nome': usuario.nome_completo
    }
    return JsonResponse(data)


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def check_authentication(request):
    if request.user.is_authenticated:
        print("Autenticado")
        return JsonResponse({'isAuthenticated': True})
    else:
        print(request)
        print(request.user)
        print("Não Autenticado")
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
            return JsonResponse({'mensagem': 'Login realizado com sucesso!'}, status=200)
        else:
            return JsonResponse({'mensagem': 'Email ou senha inválidos'}, status=401)

    return JsonResponse({'mensagem': 'Método HTTP não permitido'}, status=405)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import traceback
from .models.Usuario import Usuario
import json

@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = Usuario(
                nome_completo=data['nomeCompleto'],
                cpf=data['cpf'],
                chave_passe=data.get('chavePasse', ''),
                email=data['email'],
                estado=data['estado'],
                cidade=data['cidade']
            )
            usuario.set_password(data['senha'])  # Use o método set_password para definir a senha corretamente
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

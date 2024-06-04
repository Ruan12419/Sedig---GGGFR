from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import json
import random
import traceback
from .models import Usuario
from django.utils.decorators import method_decorator
from django.views import View
from .models.orcamentos_model import Orcamento, Patio, ModuloManobra, ModuloEquipamento
from .models.insumos_model import Insumo

def check_authentication(request):
    if request.user.is_authenticated:
        print('Usuário autenticado:', request.user)
        print('Dados da sessão:', request.session.items())
        return JsonResponse({
            'isAuthenticated': True,
            'is_superuser': request.user.is_superuser,
            'is_staff': request.user.is_staff
        })
    else:
        print(f"{request.user} Não Autenticado")
        return JsonResponse({'isAuthenticated': False})



@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(request, username=data['email'], password=data['senha'])
        print(user)
        if user is not None:
            login(request, user)
            print('ID da sessão:', request.session.session_key)
            print('Dados da sessão:', request.session.items())
            return JsonResponse({ 'mensagem': "Login realizado com sucesso!"}, status=200)
        else:
            return JsonResponse({'mensagem': 'Email ou senha inválidos'}, status=401)

    return JsonResponse({'mensagem': 'Método HTTP não permitido'}, status=405)



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



@csrf_exempt
def logout_view(request):
    print(request)
    logout(request)
    return JsonResponse({'mensagem': 'Logout realizado com sucesso!'})




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


@method_decorator(csrf_exempt, name='dispatch')
class OrcamentoCompletoView(View):
    def post(self, request):
        data = json.loads(request.body)
        usuario = request.user
        
        orcamento = Orcamento(
            nome_orcamento=data['nomeOrcamento'],
            nome_subestacao=data['nomeSubestacao'],
            macroregiao=data['macroregiao'],
            estado=data['estado'],
            ano_referencia=data['ano_referencia'],
            mes_referencia=data['mes_referencia'],
            tipo_instalacao=data['tipo_instalacao'],
            usuario=usuario
        )
        orcamento.save()

        patio = Patio(
            orcamento=orcamento,
            tensao_primaria=float(data['tensaoPrimaria']),
            arranjo=data['arranjo']
        )
        patio.save()
        print(data['modulosManobra'])
        for modulo_manobra_data in data['modulosManobra']:
            ModuloManobra(
                patio=patio,
                sincronizacao_disjuntor=modulo_manobra_data['sincDisjuntor'],
                tipo_aplicacao=modulo_manobra_data['tipoAplicacao'],
                quantidade=modulo_manobra_data['quantidade'],
                tipo=modulo_manobra_data['tipo']
            ).save()

        for modulo_equipamento_data in data['modulosEquipamento']:
            ModuloEquipamento(
                patio=patio,
                tipo_equipamento=modulo_equipamento_data['equipamento'],
                quantidade=modulo_equipamento_data['quantidade']
            ).save()

        return JsonResponse({'mensagem': 'Orçamento completo adicionado com sucesso!'}, status=201)



@login_required
def lista_orcamentos(request):
    orcamentos_data = []
    usuario = request.user
    for orcamento in Orcamento.objects.filter(usuario=usuario):
        patios = Patio.objects.filter(orcamento=orcamento)
        modulos_count = sum(ModuloManobra.objects.filter(patio=patio).count() for patio in patios) + \
                        sum(ModuloEquipamento.objects.filter(patio=patio).count() for patio in patios)
        orcamentos_data.append({
            'id': orcamento.id, 
            'nomeSubestacao': orcamento.nome_subestacao,
            'dataCotacao': f"{orcamento.ano_referencia}/{orcamento.mes_referencia}",
            'qtdPatios': patios.count(),
            'qtdModulos': modulos_count,
            'acao': '' 
        })

    return JsonResponse(orcamentos_data, safe=False)



@require_http_methods(["POST"])
@csrf_exempt
def edit_orcamento(request, orcamento_id):
    try:
        data = json.loads(request.body)
        orcamento = Orcamento.objects.get(id=orcamento_id)
        # Atualize os campos do orçamento com os dados recebidos
        orcamento.nome_subestacao = data.get('nomeSubestacao', orcamento.nome_subestacao)
        # ... atualize outros campos conforme necessário ...
        orcamento.save()
        return JsonResponse({'mensagem': 'Orçamento atualizado com sucesso!'})
    except Orcamento.DoesNotExist:
        return JsonResponse({'mensagem': 'Orçamento não encontrado.'}, status=404)

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_orcamento(request, orcamento_id):
    try:
        orcamento = Orcamento.objects.get(id=orcamento_id)
        orcamento.delete()
        return JsonResponse({'mensagem': 'Orçamento deletado com sucesso!'})
    except Orcamento.DoesNotExist:
        return JsonResponse({'mensagem': 'Orçamento não encontrado.'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class ListaInsumosView(View):
    def get(self, request):
        insumos = list(Insumo.objects.values())
        print(insumos)
        return JsonResponse(insumos, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdicionaInsumoView(View):
    def post(self, request):
        data = json.loads(request.body)
        insumo = Insumo(
            tipo_insumo=data['tipo_insumo'],
            nome=data['nome'],
            local=data['local'],
            quantidade=data['quantidade'],
            preco_unitario=data['preco_unitario'],
            custo=data['custo']
        )
        insumo.save()
        return JsonResponse({'mensagem': 'Insumo adicionado com sucesso!'}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class AtualizaInsumoView(View):
    def post(self, request, id):
        data = json.loads(request.body)
        Insumo.objects.filter(id=id).update(**data)
        return JsonResponse({'mensagem': 'Insumo atualizado com sucesso!'}, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class DeletaInsumoView(View):
    def delete(self, request, id):
        insumo = Insumo.objects.get(id=id)
        insumo.delete()
        return JsonResponse({'mensagem': 'Insumo deletado com sucesso!'}, status=200)

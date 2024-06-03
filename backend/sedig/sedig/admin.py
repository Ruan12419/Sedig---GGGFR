from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome_completo', 'cpf', 'estado', 'cidade', 'chave_passe')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Datas Importantes', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'nome_completo', 'cpf', 'estado', 'cidade', 'chave_passe', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('email', 'nome_completo', 'cpf', 'chave_passe', 'estado', 'cidade', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'nome_completo', 'cpf')
    ordering = ('email',)

admin.site.register(Usuario, UserAdmin)

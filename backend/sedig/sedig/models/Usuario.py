from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    chave_passe = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(unique=True)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo']

    objects = UsuarioManager()

    def __str__(self):
        return self.nome_completo

# Modelo de Usuário para MongoDB
# from djongo import models
#
# class Usuario(models.Model):
#     nome_completo = models.CharField(max_length=255)
#     cpf = models.CharField(max_length=14)
#     chave_passe = models.CharField(max_length=14, blank=True, null=True)
#     email = models.EmailField(unique=True)
#     estado = models.CharField(max_length=2)
#     cidade = models.CharField(max_length=255)
#     senha = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.nome_completo
#
#     class Meta:
#         app_label = 'nome_do_seu_app'

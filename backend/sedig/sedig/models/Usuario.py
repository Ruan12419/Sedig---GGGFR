from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _

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

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    chave_passe = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(unique=True)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo']

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="usuario_set", 
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="usuario_perm_set", 
        related_query_name="usuario_perm",
    )

    objects = UsuarioManager()
    
    def save(self, *args, **kwargs):
        if self.is_staff or self.is_superuser:
            if not self.chave_passe.startswith('A'):
                self.chave_passe = 'A' + self.chave_passe[1:]
        else:
            if not self.chave_passe.startswith('U'):
                self.chave_passe = 'U' + self.chave_passe[1:]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_completo
    
    def has_module_perms(self, app_label):
        return self.is_superuser

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

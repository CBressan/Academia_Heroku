from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db import models
from datetime import datetime, date


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Usuarios devem ter um email')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class Aluno_Usuario(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    nome = models.CharField(max_length=30, default='')
    sobrenome = models.CharField(max_length=30, default='')
    cpf = models.CharField(max_length=14, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_de_nascimento = models.DateField(default=datetime.now())
    endereço = models.CharField(max_length=100, default='')
    telefone = models.CharField(max_length=16, default='')
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Masculino'), (GENDER_FEMALE, 'Feminino')]
    sexo = models.IntegerField(choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    altura = models.FloatField(default=0.0)
    peso_inicial = models.FloatField(default=0.0)
    peso_atual = models.FloatField(default=0.0)
    peso_objetivo = models.FloatField(default=0.0)
    avaliações = models.TextField(null=True, blank=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

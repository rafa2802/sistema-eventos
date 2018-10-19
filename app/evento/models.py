from django.db import models
from app.core.models import UUIDUser, CreateUpdateModel

class Evento(CreateUpdateModel):
    dono = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'users', verbose_name = 'dono do evento')
    nome = models.CharField(max_length = 255, verbose_name = 'nome do evento')
    palestras = models.ManyToManyField('Atividade', related_name = 'palestras', verbose_name = 'palestras', blank=True)
    minicursos = models.ManyToManyField('Atividade', related_name = 'minicursos', verbose_name = 'minicursos', blank=True)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'

class Atividade(CreateUpdateModel):
    TIPO = (
        (0,'Palestra'),
        (1,'Minicurso')
    )
    palestrante = models.ForeignKey('Palestrante', on_delete = models.CASCADE, related_name = 'user', verbose_name = 'palestrante')
    nome = models.CharField(max_length=255, verbose_name='nome da atividade')
    duracao = models.TimeField(verbose_name='duração')
    data = models.DateField(verbose_name='data da atividade')
    hora = models.TimeField('hora da atividade')
    inscritos = models.ManyToManyField(UUIDUser, related_name='inscritos', verbose_name='inscritos', blank=True)
    tipo = models.IntegerField(choices=TIPO, verbose_name='tipo de atividade')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'atividade'
        verbose_name_plural = 'atividades'

class Palestrante(CreateUpdateModel):
    nome = models.CharField(max_length=255, verbose_name='nome do palestrante')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

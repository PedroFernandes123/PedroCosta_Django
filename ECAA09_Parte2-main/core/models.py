from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_oficina = models.BooleanField(default=False)

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class PerfilOficina(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_oficina')
    especialidades = models.ManyToManyField(Especialidade)
    nome_oficina = models.CharField(max_length=200)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_oficina

class Problema(models.Model):
    STATUS_CHOICES = (
        ('ABERTO', 'Em Aberto'),
        ('ANDAMENTO', 'Em Andamento'),
        ('CONCLUIDO', 'Concluído'),
    )

    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problemas_criados')
    oficina = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='servicos_pegos')
    titulo = models.CharField(max_length=200)
    modelo_carro = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='problemas/', null=True, blank=True, help_text='Foto do problema')
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTO')

    def __str__(self):
        return f"{self.modelo_carro} - {self.titulo}"

    def oficinas_interessadas(self):
        """Retorna todas as oficinas interessadas neste problema"""
        return self.interesses.filter(status='INTERESSADA').values_list('oficina', flat=True)
    
    def total_interessadas(self):
        """Retorna o total de oficinas interessadas"""
        return self.interesses.filter(status='INTERESSADA').count()


class Interesse(models.Model):
    STATUS_CHOICES = (
        ('INTERESSADA', 'Interessada'),
        ('REJEITADA', 'Rejeitada'),
        ('CANCELADA', 'Cancelada'),
    )
    
    problema = models.ForeignKey(Problema, on_delete=models.CASCADE, related_name='interesses')
    oficina = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interesses_manifesto')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='INTERESSADA')
    mensagem = models.TextField(blank=True, null=True, help_text='Mensagem da oficina sobre o serviço')
    data_interesse = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('problema', 'oficina')
        ordering = ['-data_interesse']

    def __str__(self):
        return f"{self.oficina.username} interessada em {self.problema.titulo}"
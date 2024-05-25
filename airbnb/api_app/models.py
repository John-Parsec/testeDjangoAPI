from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    limiteCrianca = models.IntegerField()
    limiteAdulto = models.IntegerField()
    limiteBebe = models.IntegerField()
    limitePet = models.IntegerField()

    def __str__(self):
        return self.nome

class Nivel(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Relacao(models.Model):
    inicio = models.DateField()
    fim = models.DateField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd_crianca = models.IntegerField()
    qtd_adulto = models.IntegerField()
    qtd_bebe = models.IntegerField()
    qtd_pet = models.IntegerField()

    def __str__(self):
        return f'{self.user} - {self.produto}'
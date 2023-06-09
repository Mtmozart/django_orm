from django.db import models
from django.contrib.auth import get_user_model

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero

class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome

def set_default_montadora():
    return Montadora.objects.get_or_create(nome = 'Padraozinha')[0]
class Carro(models.Model):
    """
    #OneToOneField -- Cada carro poderá ter somente um chassi o chassi com um carro, não pode repetir.

    #ForeingKey -- Cada carro terá uma montadora, mas a montadora pode ter vários carros.
    #ManyToMany - um carro pode ser dirigido por vários motoristas e o motorista pode dirigir vários carros.
    Não ao mesmo tempo. Pegação geral.

    
    montadora = models.ForeignKey(Montadora, on_delete=models.SET_DEFAULT, default=1) - esse set é para evitar que se apague o carro se apaga a montadora, 
    definirá o valor para o parâmetro default
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=30,  help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'Modelo: {self.modelo}, Montadora: {self.montadora}'







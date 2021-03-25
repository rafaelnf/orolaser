from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=500, verbose_name="Nome Completo")
    photo = models.ImageField(upload_to='banners')
    price = models.FloatField(verbose_name="Preço", default=0)
    description = models.CharField(max_length=1000, verbose_name="Descrição",null=True, blank=True)
    oroClub = models.IntegerField(verbose_name="ORO Club", default=0)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'



class Units(models.Model):
    name = models.CharField(max_length=500, verbose_name="Nome")
    address = models.CharField(max_length=500, verbose_name="Endereço")
    lat = models.FloatField(verbose_name="Latitude", default=0)
    long = models.FloatField(verbose_name="Longitude", default=0)
    photo = models.ImageField(upload_to='imagem')
    opening_hours = models.CharField(max_length=500, verbose_name="Horarios de Funcionamento")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unidade'


class Notification(models.Model):
    message = models.CharField(max_length=500, verbose_name="Mensagem")
    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Notificaçõe'

class Token(models.Model):
    token = models.CharField(max_length=500, verbose_name="Token")
    def __str__(self):
        return self.token

    class Meta:
        verbose_name = 'Token'
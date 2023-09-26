from django.db import models


class SiteDeNoticias(models.Model):
    id_site = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.nome

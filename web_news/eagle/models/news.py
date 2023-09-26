from django.db import models
from eagle.models.web_sites import SiteDeNoticias
from eagle.models.news_category import CategoriaDeNoticias


class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    id_site = models.ForeignKey(SiteDeNoticias, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(CategoriaDeNoticias, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField()
    url = models.URLField()
    relevante = models.BooleanField()

    def __str__(self):
        return self.titulo

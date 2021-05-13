from django.db import models

class Item(models.Model):
	text = models.TextField(default='')

	BAIXA = 'B'
	MEDIA = 'M'
	ALTA = 'A'
	PRIORIDADES = [
		(BAIXA, 'Baixa'),
		(MEDIA, 'Média'),
		(ALTA, 'Alta'),
	]

	prioridade = models.CharField(
		"Gênero",
		max_length=1,
		choices=PRIORIDADES,
		default=BAIXA,
	)
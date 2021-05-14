from django.shortcuts import redirect, render
from .models import Item

import string
from random import choice

def home_page(request, lista=""):
	if request.method == 'POST':
		if len(lista) == 0:
			while True:
				lista = gerar()
				if not Item.objects.filter(idlista=lista).exists():
					break
		Item.objects.create(idlista=lista, text=request.POST['item_text'], prioridade=request.POST['prioridade'])
		return redirect("".join(['/', lista]))

	items = Item.objects.filter(idlista=lista)
	return render(request, 'home.html', {'items': items})


def gerar(tamanho=20):
	valores = string.ascii_letters + string.digits
	lista = ''.join([choice(valores) for i in range(tamanho)])
	return lista
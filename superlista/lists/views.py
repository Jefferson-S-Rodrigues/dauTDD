from django.shortcuts import redirect, render
from .models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'], prioridade=request.POST['prioridade'])
		return redirect('/')

	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Product

# Create your views here.
def to_index(request):
	return redirect(reverse('products:index'))


def index(request):
	context = {
		'products' : Product.objects.all()
	}
	return render(request, 'products/index.html', context)


def show(request, id):
	context = {
		'product' : Product.objects.get(id=id)
	}
	return render(request, 'products/display_product.html', context)


def new(request):
	return render(request, 'products/new_product.html')


def edit(request, id):
	context = {
		'product' : Product.objects.get(id=id)
	}
	return render(request, 'products/edit_product.html', context)


def create(request):
	response = Product.objects.validate(**request.POST)
	if not response[0]:
		for e in response[1]:
			messages.error(request, e)

	else:
		messages.success(request, response[1])
	return redirect(reverse('products:add'))


def update(request, id):
	print id
	return redirect(reverse('products:edit', kwargs={'id': id}))


def destroy(request, id):
	Product.objects.get(id=id).delete()
	return redirect(reverse('products:index'))

from django.shortcuts import render
from .models import *
from .forms import *
from django.core.paginator import Paginator
from .filters import *

# Create your views here.

def Categoryview(request):
    page_number = request.GET.get('page')
    filter = CategoryFilter (request.GET, queryset=Category.objects.all())
    Categories = filter.qs
    paginator = Paginator(Categories, 3)
    page = paginator.get_page(page_number)

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CategoryForm()
    context = {'form':form, 'page':page}
    return render(request, 'Category.html', context)

def Unitview(request):
    Units = Unit.objects.all()
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UnitForm()
    context = {'form':form, 'uts':Units}
    return render(request, 'Unit.html', context)

def Itemview(request):
    page_number = request.GET.get('page')
    filter = ItemFilter (request.GET, queryset=Item.objects.all())
    Items = filter.qs
    paginator = Paginator(Items, 3)
    page = paginator.get_page(page_number)

    if request.method == 'POST':
        form = ItemForm(request.POST)
    else:
        form = ItemForm()
    context = {'form':form, 'page':page}
    return render(request, 'Item.html', context)

def Supplierview(request):
    Suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()
    context = {'form':form, 'Supplrs':Suppliers}
    return render(request, 'Supplier.html', context)

def Orderview(request):
    Orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    context = {'form':form, 'Ordrs':Orders}
    return render(request, 'Order.html', context)

def Employeeview(request):
    Employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    context = {'form':form, 'Employs':Employees}
    return render(request, 'Employee.html', context)

def test(request):
    if request.method == 'POST':
        form=TestForm(request.POST)
    else:
        form =TestForm()
    context = {'form':form}
    return render(request,'test.html', context)



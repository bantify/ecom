from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from store.forms import CustomerForm, ProductForm
from store.models import Customer, Product


# Create your views here.
def home(request):
    return render(request, 'store/home.html', {})


def listCustomer(request):
    customers = Customer.objects.all().order_by('updateDate')
    context = {'customers': customers}
    return render(request, template_name='store/customerList.html', context=context)


def deleteCustomer(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    customers = Customer.objects.all()
    context = {'customers': customers}
    messages.success(request, message=f"Customer {customer.name} deleted successfully.")
    return render(request, template_name='store/customerList.html', context=context)


def deleteProduct(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    products = Product.objects.all()
    context = {'products': products}
    messages.success(request, message=f"Product {product.name} deleted successfully.")
    return render(request, template_name='store/productList.html', context=context)


def addCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message=f"Customer {form.cleaned_data.get('name')} saved successfully.")
            customers = Customer.objects.all()
            context = {'customers': customers}
            return render(request, template_name='store/customerList.html', context=context)
        else:
            messages.error(request, message=form.errors)
            customerForm = form
            context = {'customerForm': customerForm}
            return render(request, template_name='store/AddCustomer.html', context=context)
    else:
        customerForm = CustomerForm()
        context = {'customerForm': customerForm}
        return render(request, template_name='store/AddCustomer.html', context=context)


def editCustomer(request, id):
    customer = Customer.objects.get(pk=id)
    customerForm = CustomerForm(instance=customer)
    context = {'customerForm': customerForm}
    return render(request, template_name='store/AddCustomer.html', context=context)


def listProduct(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name='store/productList.html', context=context)


def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            products = Product.objects.all()
            context = {'products': products}
            messages.success(request, message=f"Product {form.cleaned_data.get('name')} saved successfully.")
            return render(request, template_name='store/productList.html', context=context)
        else:
            productForm = form
            context = {'productForm': productForm}
            return render(request, template_name='store/AddProduct.html', context=context)
    else:
        productForm = ProductForm()
        context = {'productForm': productForm}
        return render(request, template_name='store/AddProduct.html', context=context)


def editProduct(request, id):
    product = Product.objects.get(pk=id)
    productForm = ProductForm(instance=product)
    context = {'productForm': productForm}
    return render(request, template_name='store/AddProduct.html', context=context)


class HomeView(TemplateView):
    def get_template_names(self):
        return "store/home.html"


class CustomerListView(ListView):
    template_name = 'store/customerList.html'
    context_object_name = 'customers'
    model = Customer


class ProductListView(ListView):
    template_name = 'store/productList.html'
    context_object_name = 'products'
    model = Product


class CustomerCreateView(SuccessMessageMixin,CreateView):
    form_class = CustomerForm
    template_name = 'store/AddCustomer.html'
    success_message = "Customer %(name)s created successfully"
    success_url = reverse_lazy("listCustomer")


class CustomerUpdateView(SuccessMessageMixin,UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'store/AddCustomer.html'
    success_message = "Customer %(name)s updated successfully"
    success_url = reverse_lazy("listCustomer")


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'store/delete_Customer_confirmation.html'
    # success_message = "Customer %(id)i deleted successfully"
    success_url = reverse_lazy("listCustomer")


class ProductCreateView(SuccessMessageMixin,CreateView):
    form_class = ProductForm
    template_name = 'store/AddProduct.html'
    success_message = "Product %(name)s created successfully"
    success_url = reverse_lazy("listProduct")


class ProductUpdateView(SuccessMessageMixin,UpdateView):
    form_class = ProductForm
    template_name = 'store/AddProduct.html'
    success_message = "Product %(name)s updated successfully"
    success_url = reverse_lazy("listProduct")

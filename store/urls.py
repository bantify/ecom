from django.urls import path
from store.views import (home, listCustomer, addCustomer, addProduct, listProduct, editProduct, deleteCustomer,
                         editCustomer, deleteProduct, HomeView, CustomerListView, ProductListView, CustomerCreateView,
                         ProductCreateView,CustomerUpdateView,CustomerDeleteView)

urlpatterns = [
    # path('', home, name="home"),
    # path('listCustomer', listCustomer, name="listCustomer"),
    path('addCustomer', addCustomer, name="addCustomer"),
    # path('listProduct', listProduct, name="listProduct"),
    # path('addProduct', addProduct, name="addProduct"),
    # path('editProduct/<int:id>', editProduct, name="editProduct"),
    # path('deleteProduct/<int:id>', deleteProduct, name="deleteProduct"),
    # path('deleteCustomer/<int:id>', deleteCustomer, name="deleteCustomer"),
    # path('editCustomer/<int:id>', editCustomer, name="editCustomer"),
    path('', HomeView.as_view(), name="home"),
    path('listCustomer', CustomerListView.as_view(), name="listCustomer"),
    path('listProduct', ProductListView.as_view(), name="listProduct"),
    # path('addCustomer', CustomerCreateView.as_view(), name="addCustomer"),
    path('addProduct', ProductCreateView.as_view(), name="addProduct"),
    path('editCustomer/<int:pk>', CustomerUpdateView.as_view(), name="editCustomer"),
    path('deleteCustomer/<int:pk>', CustomerDeleteView.as_view(), name="deleteCustomer"),
]

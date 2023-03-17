from django .urls import path
from .import views

urlpatterns = [
    path('register',views.register,name="register"),
    path('',views.login,name="login"),
    path('userHome',views.userHome,name="userHome"),
    path('logout',views.logout,name="logout"),
    path('productList',views.productList,name="productList"),
    path('newProduct',views.newProduct,name="newProduct")
]

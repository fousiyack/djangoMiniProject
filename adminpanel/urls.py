from django .urls import path
from .import views

urlpatterns = [
   
    path('',views.adminlogin,name="adminLogin"),
    path('adminHome/',views.adminHome,name="adminHome"),
    path('adminLogout/', views.adminLogout,name='adminLogout'),
    path('delete/<int:id>/', views.delete_data,name='delete_data'),
    path('<int:id>/', views.update_data,name='update_data'),
    path('createUser', views.createUser,name='createUser'),
    path('search_data', views.search_data,name='search_data'),
]
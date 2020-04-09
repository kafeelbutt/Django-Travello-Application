from django.urls import path,include
from . import views

urlpatterns=[
    
    path('dest_list',views.dest_list,name="dest_list"),
    path('view_data',views.view_data,name='view_data'),
    path('dest_view/<int:pk>',views.dest_view,name="destination_view"),
    path('create_data', views.create_data, name='create_data'),
    path('update_data/<int:pk>', views.update_data, name='update_data'),
    path('delete_data/<int:pk>', views.delete_data, name='delete_data'),
    path('accounts/',include('accounts.urls')),

]

from django.urls import path
from car_app import views



urlpatterns = [
    # path("sign_up/",views.register,name="signup"),
    path("class_vased_sign_up/",views.class_vased_register.as_view(),name="signup"),
    # path("login/",views.log_in,name='log_in'),
    
    path("login/",views.class_vased_logIn.as_view(),name='log_in'),
    
    path("logout/",views.log_out,name="log_out"),
    # path("details/<int:id>",views.details,name='details_car'),
    path("details/<int:id>",views.class_vased_details.as_view(),name='details_car'),
    path("buycar/<int:id>",views.buy_car,name='buy_car'),
    path('buy_car_details/',views.buy_car_detais,name='profile_buy_car'),
    
    
    path("user_change_data/",views.user_change_data,name="user_change_data")
   
   
]

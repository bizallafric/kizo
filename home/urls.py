from django.conf.urls import url
from django.urls import include,path
from .import views
app_name="home"

urlpatterns=[
    path('',views.homePage,name="home"),
    path('laod/deals',views.loadDeals,name="loaddeals"),
    path('home/products',views.loadproducts,name="loadhomeproducts"),
    url(r'^product/detail/(?P<slug>[\w-]+)$',views.productDetail,name="detail"),
    path('login/user',views.userLogin,name="login"),
    path('load/auth',views.loadAuth,name="userauth"),
    
]
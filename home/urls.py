from django.conf.urls import url
from django.urls import include,path
from .import views
app_name="home"

urlpatterns=[
    path('shopping/policy',views.shoppingPolicy,name="shoppingpolicy"),
     path('data/policy',views.policy,name="policy"),
    path('about/monikizo/Shop',views.about,name="about"),
    url(r'^(?P<cat>[0-9]+)/(?P<sub>[0-9]+)$',views.productSeach,name="productSearch"),
    url(r'^api/product/search/(?P<cat>[0-9]+)/(?P<sub>[0-9]+)$',views.APIproductSeach,name="APIproductSearch"),
    path('',views.homePage,name="home"),
    path('laod/deals',views.loadDeals,name="loaddeals"),
    path('home/products',views.loadproducts,name="loadhomeproducts"),
    url(r'^product/detail/(?P<slug>[\w-]+)$',views.productDetail,name="detail"),
    path('login/user',views.userLogin,name="login"),
    path('load/auth',views.loadAuth,name="userauth"),
    path('load/menu',views.LoadMenu,name="menu"),
    url(r'^load/similar/products/product/detail/(?P<slug>[\w-]+)$',views.loadSimilarProducts,name="loadhomeproducts"),
    
]
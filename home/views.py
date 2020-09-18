from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.response  import Response
from product.models import productPost,productImages
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import login,logout,authenticate
from .serializa import CreateUserSerializer
from .models import User
from rest_framework.authtoken.models import Token


#load products
@api_view(['GET'])
def loadproducts(request):
    product_list=[]
    data={}
    auth=0
    if request.user:
        auth=1

    qs = productPost.objects.all().order_by('-created')
    for x in qs :
        image_qs = productImages.objects.filter(product=x)
        for imagex in image_qs:
            pass
        print(auth)
        product_list.append({
         'auth':auth,
         'slug':x.slug,
         'name':x.productname,
         'price':x.price,
         'description':x.description,
         'state':x.productstate,
         'contact':x.contact,
         'image':'media/'+str(imagex.image),

        })
        #get the images related to x
        

    data=product_list
    return Response(data,status=200)

#load products
@api_view(['GET'])
def loadDeals(request):
    product_list=[]
    data={}
    auth=0
    if request.user:
        auth=1
    qs = productPost.objects.all().order_by('-created')
    for x in qs :
        image_qs = productImages.objects.filter(product=x)
        for imagex in image_qs:
            pass
       
        product_list.append({
         'price':x.price,
         'contact':x.slug,
         'image':'media/'+str(imagex.image),

        })
        #get the images related to x
        

    data=product_list
    return Response(data,status=200)


def homePage(request):
    template_name="home/home.html"
    context={}
    return render(request,template_name,context)


def productDetail(request,slug):
    product  = productPost.objects.get(slug=slug)
    firsimg  = productImages.objects.filter(product=product)
    if firsimg:
        firsimg=firsimg.first()
    imgs     = productImages.objects.filter(product=product)[1:]
    template_name="home/detail.html"
    context={'product':product,'imgs':imgs,'firsimg':firsimg}
    return render(request,template_name,context)

# login user 

@api_view(['POST'])
def userLogin(request,*args,**kwargs):
    serialzer  = CreateUserSerializer(data=request.data)
    data ={}
    token = None
    if serialzer.is_valid(raise_exception=True):
        number = serialzer.validated_data['phone']
        name   = serialzer.validated_data['name']
        user   = User.objects.filter(number=number)
        if not user.exists():
            
            _user   = User.objects.create(number=number,username=name)
            _user.set_password('kizoshop')
            _user.save()
            login(request,_user)

        if user:
            user= User.objects.get(number=number)
            login(request,user)         
        token =Token.objects.get(user=user)
        data={
                'token':token.key
             }  
        print(token)   
    else:
        print('error')
        data = serialzer.errors
    return Response(data,status=200)

#check for auth
@api_view(['GET'])
def loadAuth(request):
    auth=0
    if request.user.is_authenticated:
        auth=1
    data={
        'auth':auth
    }
    return Response(data,status=200)

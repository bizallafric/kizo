from django.shortcuts import render,HttpResponse
from rest_framework.decorators  import api_view
from rest_framework.response  import Response
from product.models import subCategory,category,ProductDeal,productPost,productImages
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import login,logout,authenticate
from .serializa import CreateUserSerializer
from .models import User
from rest_framework.authtoken.models import Token
from django.db.models import Q


# privacy policies
def shoppingPolicy(request):
    title="Data policy"
    description="Shopping policies of kizo shop"
    template_name="home/shoppingpolicy.html"
    context ={'title':title,'description':description}
    return render(request,template_name,context)


# privacy policies
def policy(request):
    title="Data policy"
    description="Customers data is our top priority"
    template_name="home/policy.html"
    context ={'title':title,'description':description}
    return render(request,template_name,context)

#page not found error
def handler404(request,exception):
    template_name="home/404.html"
    context={}
    return render(request,template_name,status=404)

# server does not support http request
def handler505(request):
    HttpResponse('Your http request could not be process')
# internal server error
def handler500(request):
    HttpResponse('Internal server error')

def about(request):
    title="About Monikizo"
    description=" Fine quality and durable products. Your satisfaction comes first"
    categories = category.objects.all()
    template_name="home/about.html"
    context={'description':description,'title':title,'categories':categories}
    return render(request,template_name,context)

def productSeach(request,cat,sub):
    categories = category.objects.all()
    cate= category.objects.filter(id=cat)
    title=None
    description= None
    if cate:
        cate = cate.first()
    subcate = subCategory.objects.filter(id=sub)
    if subcate:
        subcate = subcate.first()
        title ="Category:"+str(cate.name)+"Subcategory:"+str(subcate.name)
        description=" List of available products in" + "Category:"+str(cate.name)+"Subcategory:"+str(subcate.name)
    template_name="home/productSearch.html"
    context={'description':description,'title':title,'categories':categories,'subcate':subcate,'cate':cate}
    return render(request,template_name,context)

# display products base on product category and product subcategory
@api_view(['GET'])
def APIproductSeach(request,cat,sub):
    print('Api searhc product')
    cat = category.objects.filter(id=cat)
    cat = cat.first()
    sub =  subCategory.objects.filter(id=sub)
    sub = sub.first()
    qs  = productPost.objects.filter(cat=cat,subcat=sub).order_by('-created')
    product_list=[]
    for x in qs :
        image_qs = productImages.objects.filter(product=x)
        for imagex in image_qs:
            pass
        
        product_list.append({
         
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

# load similar products
@api_view(['GET'])
def loadSimilarProducts(request,slug):
    product_list=[]
    data={}
    auth=0
    if request.user:
        auth=1
    qs = productPost.objects.get(slug=slug)
    qs = productPost.objects.filter(Q(productname=qs.productname)|Q(subcat=qs.subcat) | Q(brand=qs.brand)).exclude(id=qs.id).order_by('-created')
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
    qs = productPost.objects.filter(Q(hotdeal=True)|Q(dealoftheday=True)).order_by('-created')
    for x in qs :
        image_qs = productImages.objects.filter(product=x)
        for imagex in image_qs:
            pass
       
        product_list.append({
         'price':x.price,
         'contact':'/product/detail/'+x.slug,
         'image':'media/'+str(imagex.image),

        })
        #get the images related to x
        

    data=product_list
    return Response(data,status=200)




def homePage(request):
    title="monikizo Shop"
    description ="Fine quality and durable products. Your satisfaction comes first"
    categories = category.objects.all()
    template_name="home/home.html"
    context={'title':title,'description':description,'categories':categories}
    return render(request,template_name,context)

    
# display products base on product category and product subcategory
def productDetail(request,slug):
    categories = category.objects.all()
    product  = productPost.objects.get(slug=slug)
    firsimg  = productImages.objects.filter(product=product)
    title=None
    description=None
    if product:
        title = str(product.productname)
        description=str(product.description)
    if firsimg:
        firsimg=firsimg.first()
    imgs     = productImages.objects.filter(product=product)[1:]
    # load product deals
    productdeal    = ProductDeal.objects.filter(product=product)
    template_name="home/detail.html"
    context={'title':title,'description':description,'categories':categories,'productdeal':productdeal,'product':product,'imgs':imgs,'firsimg':firsimg}
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

#get product menus
@api_view(['GET'])
def LoadMenu(request):
    categories = category.objects.all()
    data ={}
    mainmenu=[]
    submenu = []
    for cat in categories:
        
        cats={
            'category':cat.name,
            'category_id':cat.id,
        }
        mainmenu.append(cats)
    print(data)
   
    return Response(data,status=200)

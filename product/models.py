from django.db import models
from .slug import Generate_slug

class category(models.Model):
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name


class subCategory(models.Model):
    name = models.CharField(max_length=200,null=True)
    cat  = models.ForeignKey(category,on_delete=models.CASCADE,null=True,related_name="sub_cat")
    def __str__(self):
        return self.name


class productPost(models.Model):
    images      = models.ManyToManyField
    created     = models.DateTimeField(auto_now_add=True,null=True)
    updated     = models.DateTimeField(auto_now=True,null=True)
    cat    = models.ForeignKey(category,on_delete=models.CASCADE,null=True,related_name="product_cat",blank=True)
    subcat      = models.ForeignKey(subCategory,on_delete=models.CASCADE,null=True,related_name="product_subcategory",blank=True)
    brand       = models.CharField(max_length=200,null=True)
    model       = models.CharField(max_length=200,null=True)
    color       = models.CharField(max_length=200,null=True)
    productname = models.CharField(max_length=200,null=True)
    storage     = models.CharField(max_length=200,null=True)
    size        = models.CharField(max_length=200,null=True)
    color       = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    slug        = models.CharField(max_length=200,null=True,blank=True)
    price       = models.CharField(max_length=100,null=True)
    productstate= models.CharField(max_length=100,null=True)
    contact     = models.CharField(max_length=100,null=True,help_text="(237)(number)")
    hotdeal     = models.BooleanField(default=False)
    dealoftheday= models.BooleanField(default=False)
    def __str__(self):
        return self.productname

    def save(self,*args,**kwargs):
        if self.id is None:
            instance = self
            slug= self.productname
            self.slug=Generate_slug(instance,slug)
        
        return super(productPost,self).save(*args,**kwargs)

class ProductDeal(models.Model):
    dealname     = models.CharField(max_length=200,null=True)
    product      = models.ForeignKey(productPost,blank=True,on_delete=models.CASCADE,null=True,related_name="productdeal")
    dealimg     = models.ImageField(upload_to="dealimg",null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.dealname



class productImages(models.Model):
    image        = models.ImageField(upload_to="images",null=True)
    product      = models.ForeignKey(productPost,on_delete=models.CASCADE,null=True,related_name="productimages")

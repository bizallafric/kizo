from django.db import models
from .slug import Generate_slug
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile

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
    created     = models.DateTimeField(auto_now_add=True,null=True,help_text="select product category")
    updated     = models.DateTimeField(auto_now=True,null=True)
    cat    = models.ForeignKey(category,on_delete=models.CASCADE,null=True,related_name="product_cat")
    subcat      = models.ForeignKey(subCategory,on_delete=models.CASCADE,null=True,related_name="product_subcategory",help_text="select product sub category")
    sellername  = models.CharField(max_length=200,null=True)
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
    hotdeal     = models.BooleanField(default=False,help_text="click if there is a gift out for this product")
    dealoftheday= models.BooleanField(default=False,help_text="click if there is a gift out for this product")
    def __str__(self):
        return self.productname

    def save(self,*args,**kwargs):
        if self.id is None:
            instance = self
            slug= self.productname
            self.slug=Generate_slug(instance,slug)
        
        return super(productPost,self).save(*args,**kwargs)

class ProductDeal(models.Model):
    dealname     = models.CharField(max_length=200,null=True,help_text="deal name example free winex as gift")
    product      = models.ForeignKey(productPost,blank=True,on_delete=models.CASCADE,null=True,related_name="productdeal")
    dealimg     = models.ImageField(upload_to="dealimg",null=True,help_text="picture of the gift")
    description = models.TextField(null=True,blank=True,help_text="description of the gift")

    def __str__(self):
        return self.dealname



class productImages(models.Model):
    image        = models.ImageField(upload_to="images",null=True)
    product      = models.ForeignKey(productPost,on_delete=models.CASCADE,null=True,related_name="productimages")
    
    def save(self,*args,**kwargs):
        self.image = compressImage(self.image)
        return super(productImages,self).save(*args)


def compressImage(uploadedImage):
    imageTemproary = Image.open(uploadedImage)
    width,height=imageTemproary.size
    outputIoStream = BytesIO()
    imageTemproaryResized = imageTemproary.resize( (300,400) )
    imageTemproaryResized.save(outputIoStream , format='JPEG', quality=100)   
    print(imageTemproaryResized.size)
    outputIoStream.seek(0)
    uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    return uploadedImage
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    def create_user(self,number,password=None,is_active=True,is_admin=False,is_staff=False):
        user = self.model(number=number)
        if not password:
            raise ValueError('User must have a  password')
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self,number,password=None):
        user = self.create_user(number,password=password,is_admin=True,is_staff=True)
        return user
    
class User(AbstractBaseUser):
    created      = models.DateField(auto_now_add=True,null=True)
    slug         = models.SlugField(null=True)
    dp           = models.ImageField(upload_to="profileimage")
    email        = models.EmailField(null=True,unique=True)
    username     = models.CharField(null=True,max_length=200)
    number       = models.IntegerField(unique=True,null=True)
    active       = models.BooleanField(default=True)
    admin        = models.BooleanField(default=False)
    staff        = models.BooleanField(default=False)
    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS=[]
    objects = UserManager()

    class Meta:
        managed=True
    def __str__(self):
        return str(self.number or None)
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_seller(self):
        return self.seller

    @property
    def is_admin(self):
        return self.admin

'''
save user other important info
'''

class UserInfo(models.Model):
    user     = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="userinfo")
    address  = models.CharField(max_length=225,null=True)
    town     = models.CharField(max_length=200,null=True)
    country  = models.CharField(max_length=225,null=True)
    areacode = models.CharField(max_length=100,null=True)
    phone    = models.CharField(max_length=200,null=True)
    def __str_(self):
        return self.user.email

# call this signal when a new user is created
@receiver(post_save,sender=User)
def createUserAccount(sender,instance=None,created=False,**kwargs):
    if  created:
        # user is agent, create agent number
        Token.objects.create(user=instance)






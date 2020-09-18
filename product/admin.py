from django.contrib import admin
from .models import productImages,productPost,category,subCategory


admin.site.register(category)
admin.site.register(subCategory)
admin.site.register(productPost)
admin.site.register(productImages)
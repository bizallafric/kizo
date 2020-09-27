from django.contrib import admin
from .models import ProductDeal,productImages,productPost,category,subCategory

class dealInline(admin.StackedInline):
    model = ProductDeal

class imageInline(admin.StackedInline):
    model = productImages

class DealAdmin(admin.ModelAdmin):
    inlines=(
        dealInline,imageInline
    )
admin.site.register(productPost,DealAdmin)
admin.site.register(category)
admin.site.register(subCategory)




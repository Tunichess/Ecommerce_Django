from django.contrib import admin
from products.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug','description','price','timestamp','categorie','for_woman']
    list_editable=['categorie','for_woman']


    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin)


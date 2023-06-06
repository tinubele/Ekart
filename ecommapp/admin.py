from django.contrib import admin
from ecommapp.models import Product,OrderHistory,Order

# Register your models here.
#admin.site.register(Product)



#define Model admin class
class ProductAdminClass(admin.ModelAdmin):
    list_display=['name','cat','price','status']
    list_filter=['status','cat']
admin.site.register(Product,ProductAdminClass)
admin.site.site_header="EkartDashboard"
admin.site.register(Order)
admin.site.register(OrderHistory)




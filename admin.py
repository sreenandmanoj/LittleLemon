from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','name','guest_num','booking_date']
    search_fields = ['name']

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','inventory']
    search_fields = ['title']
    
admin.site.register(Booking,BookingAdmin)
admin.site.register(Menu,MenuAdmin)
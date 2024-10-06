from django.contrib import admin
from .models import *
# Register your models here.

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1  # Number of empty forms to display initially

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [SubcategoryInline]  # Include the inline model admin



admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(SliderItem)
admin.site.register(Cart)
admin.site.register(Sales)

from django.contrib import admin

# Register your models here.
from .models import Company
from .models import Menu
from .models import Item
from .models import Ingrediant

admin.site.register(Ingrediant)


class ItemInline(admin.StackedInline):
    model = Item
    extra = 3

class MenuInline(admin.StackedInline):
    model = Menu
    extra = 3

class IngrediantInline(admin.StackedInline):
    model = Ingrediant
    extra = 3

class MenuAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

class CompanyAdmin(admin.ModelAdmin):
    inlines =[MenuInline]

class ItemAdmin(admin.ModelAdmin):
    inlines = [IngrediantInline]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)

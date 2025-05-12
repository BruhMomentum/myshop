from django.utils.html import format_html
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'company', 'price', 'productcount', 'isdiscounted', 'display_image']
    list_filter = ['isdiscounted', 'company']
    fields = ['productname', 'company', 'productcount', 'price', 'isdiscounted', 'image', 'slug']
    prepopulated_fields = {'slug': ('productname',)}

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "Нет изображения"

    display_image.short_description = 'Изображение'

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['productname', 'slug', 'company', 'productcount', 'price', 'isdiscounted']  # Отображаемые поля в списке
#     list_filter = ['company', 'isdiscounted']  # Фильтры справа
#     list_editable = ['price', 'productcount', 'isdiscounted']  # Поля, доступные для редактирования в списке
#     search_fields = ['productname','company']  # Поиск по названию и компании
#     ordering = ['productname']  # Сортировка по умолчанию
#     prepopulated_fields = {'slug': ('productname',)}
    
#     # Настройка отображения полей при создании/редактировании
#     fieldsets = (
#         ('Основная информация', {
#             'fields': ('productname', 'company')
#         }),
#         ('Параметры товара', {
#             'fields': ('price', 'productcount', 'isdiscounted', 'slug')
#         }),
#     )

#     # def product_image(self, obj):
#     #     if obj.image:
#     #         return 'Да'
#     #     return 'Нет'
#     # product_image.short_description = 'Изображение'



from django.contrib import admin

from .models import Client, Order, Product


@admin.action(description="Сбросить количество к одному")
def reset_qnt(modeladmin, request, queryset):
    queryset.update(qnt=1)


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number"]
    ordering = ["name", "registration_date"]
    list_filter = ["name"]
    search_fields = ["email"]
    search_help_text = "Поиск по полю email"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "qnt"]
    ordering = ["title", "-price"]
    list_filter = ["title", "price"]
    search_fields = ["description"]
    search_help_text = "Поиск по полю описание"
    readonly_fields = ["creation_date"]
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["title"],
            },
        ),
        (
            "Подробности",
            {
                "classes": ["collapse"],
                "description": "Подробности о товаре",
                "fields": ["description", "price", "qnt"],
            },
        ),
        (
            "Служебная информация",
            {
                "fields": ["creation_date", "image"],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "total_price", "date_ordered"]
    ordering = ["customer", "-date_ordered"]
    list_filter = ["customer", "date_ordered"]
    search_fields = ["customer"]
    search_help_text = "Поиск по полю покупатель"


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

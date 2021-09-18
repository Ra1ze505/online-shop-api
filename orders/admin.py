from django.contrib import admin
from .models import Order, OrderItem
from django.utils.html import format_html
from django.urls import path, reverse
from django.shortcuts import redirect
from .service import send_email_status


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', 'approve_button']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    @staticmethod
    def approve_button(self):
        kwargs = {'id': self.pk,
                  'email': self.email,
                  'status': self.status.id}
        return format_html(
            f'<a class="button" href="{reverse("admin:order_apr", kwargs=kwargs)}">Уведомить</a>')
    # Добавляем к существующим ссылкам в админке, ссылки на кнопки для их обработки

    def get_urls(self):
        urls = super().get_urls()
        shard_urls = [path('apr/<int:id>/<str:email>/<int:status>/', self.admin_site.admin_view(self.set_approve), name="order_apr")]
        # Список отображаемых столбцов
        return shard_urls + urls

    # Обработка событий кнопок
    @staticmethod
    def set_approve(request, **kwargs):
        if kwargs['id'] != 0:
            # Поиск обьекта
            order = Order.objects.get(pk=kwargs['id'], email=kwargs['email'], status__id=kwargs['status'])
            if order:
                # если найден вызываем необходимый нам метод
                send_email_status(order)
        # В конце в любом случае делаем редирект на страницу обьектов
        return redirect(reverse("admin:orders_order_changelist"))


admin.site.register(Order, OrderAdmin)

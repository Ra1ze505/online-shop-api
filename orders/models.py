from django.db import models
from shop.models import Product
from main.models import Status


delivery_choise = (
        ('S', 'Самовывоз'),
        ('R', 'Почта россии'),
        ('C', 'Сдэк'),
        ('B', 'Boxberry'),
    )


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True)
    delivery = models.CharField(max_length=1, choices=delivery_choise, verbose_name='Требуется доставка?')
    address_PVZ = models.CharField(max_length=250, verbose_name='Пункт самовывоза', blank=True)
    address = models.CharField(max_length=250, verbose_name='Адрес', blank=True)
    postal_code = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Почтовый индекс', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='Город', blank=True)
    region = models.CharField(max_length=100, verbose_name='Регион/Область', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итоговая стоимость', blank=True, null=True)
    url_pay = models.URLField(verbose_name='Ссылка для оплаты', default=None, blank=True, null=True)
    paid = models.BooleanField(default=False)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE, default=1, blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

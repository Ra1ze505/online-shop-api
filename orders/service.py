from django.conf import settings
from django.core.mail import send_mail

def send_email_status(order):
    subject = f'Привет {order.first_name} {order.last_name}'
    message = f'Статус вашего заказа: {order.status}<br> Ссылка на оплату {order.total_price}: {order.url_pay}'
    from_email = settings.EMAIL_HOST_USER
    to_email = order.email
    send_mail(subject, message, from_email, [to_email], html_message=message)
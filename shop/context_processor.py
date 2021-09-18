from main.models import Container, Category


def container(request):
    return {
        'categorys': Category.objects.all(),
        'containers': Container.objects.all(),
    }
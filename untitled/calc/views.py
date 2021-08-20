from django.http import HttpResponse
from django.views import View

class CalcView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')

# Здесь view возвращает HttpResponse с указанным телом ответа,
# вместо того чтобы использовать шаблон.
# В модуле django.http вы найдёте JsonResponse, позволяющий возвращать
# данные в виде JSON и FileResponse, нужный для отправки клиенту файлов.

# Create your views here.

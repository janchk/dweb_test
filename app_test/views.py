import atexit
from django.http import JsonResponse
from app_test.models import ActiveTasks
from app_test.statistics import db_handler_th


def rqst_hndlr(request):
    try:
        db_handler_th.start()
    except:
        pass
    try:
        request.POST['data']
    except:
        return JsonResponse({'Statistics': '1'})
    ActiveTasks(curr_state='В ОЧЕРЕДИ').save()

    return JsonResponse({'Task': 'created'})


def stat_view(request):
    at_list = list(ActiveTasks.objects.values('curr_state', 'time_start'))

    return JsonResponse({'tabl': [at_list]})


def clear_table():
    ActiveTasks.objects.all().delete()

atexit.register(clear_table)

import threading
import time
import logging
from django.utils import timezone
from app_test.models import ActiveTasks, Tasks


def tsk_hndlr(tsk_id, create_time):
    ActiveTasks(curr_state='ВЫПОЛНЯЕТСЯ', time_start=create_time, id=tsk_id).save()
    exec(open("app_test/test.py").read())
    endtime = timezone.now()
    ActiveTasks(curr_state='ЗАВЕРШЕНА', time_start=create_time, time_stop=endtime,
                id=tsk_id).save()
    Tasks(id=tsk_id, create_time=create_time, finish_time=endtime).save()


def db_handler():
    while True:
        at_count = ActiveTasks.objects.filter(curr_state='ВЫПОЛНЯЕТСЯ').count()
        pt = ActiveTasks.objects.filter(curr_state='В ОЧЕРЕДИ').first()  # pendingtasks
        if at_count < 2:  # number of active tasks
            try:
                tsk_hndlr_th = threading.Thread(target=tsk_hndlr, args=(pt.id, pt.time_start))
                tsk_hndlr_th.start()
            except:
                logging.warning(pt)
        time.sleep(1)


db_handler_th = threading.Thread(target=db_handler)



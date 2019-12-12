import threading
import time
import schedule
import pandas as pd
import numpy as np


def job():
    print('Present time is: ', time.strftime("%H:%M:%S"))
    dt = np.array([])
    df = pd.DataFrame()
#    print("I'm running on thread %s" % threading.current_thread())


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(10).seconds.do(run_threaded, job)
#schedule.every(10).seconds.do(run_threaded, job)
#schedule.every(10).seconds.do(run_threaded, job)
#schedule.every(10).seconds.do(run_threaded, job)
#schedule.every(10).seconds.do(run_threaded, job)


while True:
    schedule.run_pending()

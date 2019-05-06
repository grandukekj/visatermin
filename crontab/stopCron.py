from crontab import CronTab
import os.path

def success_func(filename):
    with open(filename, 'r') as f:
        return f.readlines()[-1][-3]

if os.path.isfile('/Users/kwangjun/PycharmProjects/TerminBuchen/trial_log.txt'):
    stopsign = success_func('/Users/kwangjun/PycharmProjects/TerminBuchen/trial_log.txt')
    if stopsign == 'success':
        my_cron = CronTab(user='kwangjun')
        for job in my_cron:
            if job.comment == 'test':
                my_cron.remove_all()
                my_cron.write()
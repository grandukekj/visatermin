from crontab import CronTab

my_cron = CronTab(user='kwangjun')
job = my_cron.new(command = 'python /Users/kwangjun/PycharmProjects/TerminBuchen/log.py')
job.minute.every(1)
print job.is_valid()
# job2 = my_cron.new(command = 'python stopCron.py', comment='test2')
# job2.minute.every(1)
my_cron.write()
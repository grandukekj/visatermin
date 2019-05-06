from datetime import datetime
import os.path
import numpy as np

if os.path.isfile('/Users/kwangjun/PycharmProjects/TerminBuchen/trial_log.txt') != 1:
    with open('/Users/kwangjun/PycharmProjects/TerminBuchen/trial_log.txt', 'w') as f:
        rds = np.random.choice(['s','f'], p=[0.3,0.7])
        print rds
        f.write('Accessed on %s %d %s \n' % (str(datetime.now()), 1, rds))

else:
    with open('/Users/kwangjun/PycharmProjects/TerminBuchen/trial_log.txt', 'r+') as f:
        n = len(f.readlines()) + 1
        rds = np.random.choice(['s','f'], p=[0.3,0.7])
        print rds
        f.write('Accessed on %s %d %s \n' % (str(datetime.now()), n, rds))
import time;

localtime = time.localtime(time.time())
print ("Local current time :\n", localtime)


localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :\n", localtime)

import datetime

x = datetime.datetime.now()

print(x.strftime("%c"))

init_water = time()
print("init_water")
from datetime import datetime
from redisConnection import redisClient, STREAM_NAME
import time

while 1 > 0:
    current_dateTime = datetime.now().timestamp()
    redisClient.xadd(name=STREAM_NAME, fields={ "dev": "Arlan", "datetime": current_dateTime })
    print("Sent {0:.0f}".format(current_dateTime))
    time.sleep(0.00001)

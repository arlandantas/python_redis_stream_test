from redisConnection import redisClient, STREAM_NAME

last_read=b"$"

while 1 > 0:
    print("Last read: {}".format(last_read.decode("utf-8")))
    reads = redisClient.xread(streams={ STREAM_NAME: last_read },count=10,block=0)
    if (len(reads) > 0):
        data = reads[0][1]
        for item in data:
            last_read = item[0]
            print("Found {}: {:.0f}".format(item[0].decode("utf-8"), float(item[1][b"datetime"])))
    else:
        print("Nothing found...")

### Python Redis Stream Tests
Test only project to study python redis stream connection.

### Dependencies
```bash
$ pip install redis[hiredis]
```

### How to test
Start the consumer in one terminal: `python3 consumer.py`.

Start the producer in another one terminal: `python3 producer.py`.

OBS: If you want to start a local redis server, it is a good way to do that: `docker run --rm --name redis-server -p 6379:6379 redis/redis-stack-server:latest`

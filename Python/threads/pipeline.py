import random
import concurrent.futures
import time
import threading

FINISH = 'THE END'
producer_pipeline = []
consumer_pipeline = []

# This class is a FIFO queue, we can store only 1 value at a time,
# the capacity here just only to loop purposes.
# We can store 1 message, and we can't not store more messages until
# previous one is released.


class Pipeline:

    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        # We need to lock the consumer until producer
        # has put one value at least.
        self.consumer_lock.acquire()

    def set_message(self, message):
        print('producing message of {0}'.format(message))
        # When we insert a message into the pipeline,
        # we want to block new producers until the message
        # has been extracted
        self.producer_lock.acquire()
        producer_pipeline.append(message)
        # Once we have extracted the message we can release
        # the lock for consuming
        self.consumer_lock.release()
        self.message = message

    def get_message(self):
        print('consuming message of {0}'.format(self.message))
        self.consumer_lock.acquire()
        message = self.message
        self.producer_lock.release()
        consumer_pipeline.append(message)
        return message


def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1, 100)
        pipeline.set_message(message)
    pipeline.set_message(FINISH)


def consumer(pipeline):
    message = None
    while message is not FINISH:
        message = pipeline.get_message()
        if message is not FINISH:
            time.sleep(random.random())

if __name__ == '__main__':
    pipeline = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline)
        ex.submit(consumer, pipeline)
    print('producer {0}'.format(producer_pipeline))
    print('consumer {0}'.format(consumer_pipeline))

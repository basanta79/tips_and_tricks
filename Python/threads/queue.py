import random
import concurrent.futures
import time
import threading
import queue

producer_pipeline = []
consumer_pipeline = []

# Queue class manages authomatically the locks.
# Put and Get methods are used to enqueue and dequeue messages


class Pipeline(queue.Queue):

    def __init__(self):
        super().__init__(max_size=10)

    def set_message(self, message):
        print('producing message of {0}'.format(message))
        self.put(message)
        producer_pipeline.append(message)

    def get_message(self):
        message = self.get()
        print('consuming message of {0}'.format(message))
        consumer_pipeline.append(message)
        return message


def producer(pipeline, event):
    while not event.is_set():
        message = random.randint(1, 100)
        pipeline.set_message(message)


def consumer(pipeline, event):
    while not pipeline.empty() or not event.is_set():
        print('queue size is {0}'.format(pipeline.qsize()))
        message = pipeline.get_message()
        time.sleep(random.random())


if __name__ == '__main__':
    pipeline = Pipeline()
    # Thats a boolean flag can be event.set() and event.clear()
    # to manage this flag.
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline, event)
        ex.submit(consumer, pipeline, event)
        time.sleep(0.5)
        event.set()
    print('producer {0}'.format(producer_pipeline))
    print('consumer {0}'.format(consumer_pipeline))

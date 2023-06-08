import threading
import time
import redis
import httpx
from datetime import timedelta


def set_content(website):
    response = httpx.get(f"https://{website}/").content
    rds = redis.Redis(decode_responses=True)
    rds.set(name=website, value=response, ex=timedelta(seconds=60))


start = time.time()
thread1 = threading.Thread(target=set_content, args=('kun.uz',))
thread2 = threading.Thread(target=set_content, args=('qalampir.uz',))
thread3 = threading.Thread(target=set_content, args=('stadion.uz',))
thread4 = threading.Thread(target=set_content, args=('daryo.uz',))
thread5 = threading.Thread(target=set_content, args=('sqb.uz',))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
print("Total time:", f"{time.time() - start:.5f}")
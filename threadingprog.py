import threading
import time

# def task(name):
#     for i in range(3):
#         print(f"Task - {name}, iteration - {i}")
#         time.sleep(1)
        
# t1 = threading.Thread(target=task, args=("A",))
# t2 = threading.Thread(target=task, args=("B",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("all task completed!")

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
            
threads = [threading.Thread(target=increment) for _ in range(2)]

for t in threads:
    t.start()
    
for t in threads:
    t.join()
    
print("final counter: ", counter)
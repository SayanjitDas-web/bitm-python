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

# counter = 0
# lock = threading.Lock()

# def increment():
#     global counter
#     for _ in range(100000):
#         with lock:
#             counter += 1
            
# threads = [threading.Thread(target=increment) for _ in range(2)]

# for t in threads:
#     t.start()
    
# for t in threads:
#     t.join()
    
# print("final counter: ", counter)

# Exercise 1 — Parallel Countdown Timer
# Goal:
# Run multiple countdown timers simultaneously using threads.
# output:
# Timer A: 5
# Timer B: 3
# Timer A: 4
# Timer B: 2

def countdown(name,sec):
    while sec > 0:
        print(f"Timer {name}: {sec}")
        time.sleep(1)
        sec -= 1
        
    print(f"Timer {name} finished!")
    
timer1 = threading.Thread(target=countdown,args=("A",5))
timer2 = threading.Thread(target=countdown,args=("B",3))

timer1.start()
timer2.start()

timer1.join()
timer2.join()

print("all timer finished")
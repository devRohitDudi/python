import time

wait_time = 2
attempts = 0
max_attempts = 5

while attempts<max_attempts:
    print("attempts:",attempts+1,"wait time: T-",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempts +=1
    if(attempts==max_attempts):
        print("Now you can try again! the time was for you security.")
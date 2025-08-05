import time

wait_time = 1
max_retries = 5
attempt = 1

while attempt <= max_retries:
    print('Your Attempt - ',attempt ,'your Wait-time -',wait_time)
    attempt+=1
    time.sleep(wait_time)
    wait_time*=2

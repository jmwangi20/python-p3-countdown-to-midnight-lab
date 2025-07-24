# your code goes here!

import time 

def countdown(num):
    for i in range(num,0,-1):
        print(f'{i}SECOND(S)!')

print("HAPPY NEW YEAR!")

def countdown_with_sleep(num):
    for i in range(num,0,-1):
        print(f'{i}SECOND(S)!')
        time.sleep(2)
    

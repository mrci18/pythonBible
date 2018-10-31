import time 
#Coordinated Universal Time is 7 hours ahead of Pacific Time
#print epoch timestamp
print(time.time())

def calc_prod():
    product = 1 
    for i in range(1, 100000):
        product *= i
    return i

start_time = time.time()
x = calc_prod()
end_time = time.time()
round(end_time, 2)

print("Result is %s" % str(x))
print("It took %s seconds to run" % (end_time - start_time))

for i in range(3):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)
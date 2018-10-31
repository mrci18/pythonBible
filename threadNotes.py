import threading, time

print("Start of program")

def take_a_nap():
    print("Hey")
    time.sleep(5)
    print("Wake up")

threadObj = threading.Thread(target=take_a_nap)
threadObj.start()

print("End program")
#A Python program will not terminate until all its threads have terminated

#Multi threading can cause concurrency issues
#This is when variables are being read and written on at the same time
#Never let multiple threads read and write to the same variable
def print_list(*args, **kwargs):
    print(args)

thread2 = threading.Thread(target=print_list, args=['cats', 'dogs', 'birds'], kwargs={'sep': ' & '})
thread2.start()
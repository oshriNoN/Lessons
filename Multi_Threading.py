import threading
import time

def print_hi(num):
    for i in range(num):
        print("hi")
        time.sleep(0.03)


def print_100(num):
    for i in range(num+1):
        print(i)
        time.sleep(0.03)


if __name__ =="__main__":
    t1 = threading.Thread(target=print_hi, args=(100,))
    t2 = threading.Thread(target=print_100, args=(100,))

    t1.start()
    time.sleep(0.2)
    t2.start()

    t1.join()
    t2.join()

    print("Done!")

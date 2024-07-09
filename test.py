import threading
import time

# Global variable to control the loop in main()
done = False

def main():
    global done
    while not done:
        print("!!!!!")
        time.sleep(1)  # Simulate some work
    print("Main thread stopped.")

def catch():
    global done
    input("Press Enter to stop the main thread...\n")
    done = True
    print("Catch thread stopped.")

if __name__ =="__main__":
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=catch)
    
    t1.start()
    t2.start()
    
    t1.join()  # Wait for main() thread to finish (which it will when done is True)
    t2.join()  # Wait for catch() thread to finish
    
    print("All threads stopped. Exiting program.")
import threading

def print_hello():
    for _ in range(5):
        print("Hello")

def print_hi():
    for _ in range(5):
        print("Hi")

# Create two thread objects
thread_hello = threading.Thread(target=print_hello)
thread_hi = threading.Thread(target=print_hi)

# Start both threads
thread_hello.start()
thread_hi.start()

# Wait for both threads to finish
thread_hello.join()
thread_hi.join()

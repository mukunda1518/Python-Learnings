# Based on resource - https://arpit.substack.com/p/writing-good-multi-threaded-programs


# ------------------------------- Approach 1 ------------------------------

import threading
import math
import time


def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(current_num, limit, result, index, lock):
    start_time = time.time()
    local_count = 0
    while True:
        with lock:
            if current_num > limit:
                break
            num = current_num
            current_num += 1
        if is_prime(num):
            local_count += 1

    result[index] = local_count
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Thread {index} completed: ({local_count}), Time taken: {execution_time} seconds")
    print(f"Thread {index} completed: ({local_count}), Time taken: {execution_time//60:.2f} minutes")

def main():
    """Main function to divide workload among multiple threads."""
    N = 100000
    NUM_THREADS = 10

    threads = []
    result = [0] * NUM_THREADS
    lock = threading.Lock()
    current_num = 2

    for i in range(NUM_THREADS):
        thread = threading.Thread(target=count_primes, args=(current_num, N, result, i, lock))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    total_primes = sum(result)
    print(f"Total prime numbers up to {N}: {total_primes}")


if __name__ == "__main__":
    main()
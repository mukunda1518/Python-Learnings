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


def count_primes(start, end, result, index):
    start_time = time.time()
    result[index] = sum(1 for i in range(start, end) if is_prime(i))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Thread {index} completed: Range({start}-{end}), Time taken: {execution_time} seconds")
    print(f"Thread {index} completed: Range({start}-{end}), Time taken: {execution_time//60:.2f} minutes")

def main():
    """Main function to divide workload among multiple threads."""
    N = 5_000_000
    NUM_THREADS = 10

    threads = []
    result = [0] * NUM_THREADS
    range_size = N // NUM_THREADS

    for i in range(NUM_THREADS):
        start = i * range_size
        end = N + 1 if i == NUM_THREADS - 1 else (i + 1) * range_size
        thread = threading.Thread(target=count_primes, args=(start, end, result, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    total_primes = sum(result)
    print(f"Total prime numbers up to {N}: {total_primes}")


if __name__ == "__main__":
    main()
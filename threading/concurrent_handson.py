import time
import concurrent.futures


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds....")
    time.sleep(seconds)
    return "Done sleeping...."


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")

import time
import concurrent.futures


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds....")
    time.sleep(seconds)
    return f"Done sleeping....{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    res = executor.map(do_something, secs)
    for res in results:
        print(res)


finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")

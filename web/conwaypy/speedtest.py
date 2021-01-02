import conway
from timeit import default_timer as timer

N = 2 ** 12
data = [[False for _ in range(N)] for _ in range(N)]
print("grid NxN, N =", N)

def measure_time_evolved(thread_count):
    start = timer()
    conway.evolve(data, thread_count)
    end = timer()
    return round(end - start, 4)

threads = [1, 2, 4]
for thread in threads:
    print('{} thread: {} s'.format(thread, measure_time_evolved(thread)))
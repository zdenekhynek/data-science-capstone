import time


class Benchmarks:
    def __init__(self):
        self.t = time.process_time()
        self.benchmarks = []

    def add_benchmark(self, operation=''):
        time_lapsed = time.process_time() - self.t
        self.t = time.process_time()

        benchmark = {'id': operation, 'time': time_lapsed}
        print(benchmark)
        self.benchmarks.append(benchmark)

    def get_benchmarks(self):
        return self.benchmarks

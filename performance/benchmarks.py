import time


class Benchmarks:
    """
    Convenient way of measuing excution time between
    Calling add_benchmark will print out time lapsed since calling
    add_benchmark the last time
    """

    def __init__(self):
        self.t = time.process_time()
        self.benchmarks = []

    def add_benchmark(self, operation=''):
        # calculate time lapsed since the last time add_benchmark was called
        time_lapsed = time.process_time() - self.t

        # store the current time
        self.t = time.process_time()

        benchmark = {'id': operation, 'time': time_lapsed}

        # print out time lapsed
        print(benchmark)

        # store the benchmakr so that all benchmarks can be all retrieved
        # once it's setup
        self.benchmarks.append(benchmark)

    def get_benchmarks(self):
        return self.benchmarks

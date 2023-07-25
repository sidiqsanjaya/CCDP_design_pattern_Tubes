# pola behavioral

class SpeedTestStrategy:
    def run_test(self):
        pass

class KecepatanTestStrategy(SpeedTestStrategy):
    def run_test(self):
        print("Mengukur kecepatan internet...")

class PingTestStrategy(SpeedTestStrategy):
    def run_test(self):
        print("Mengukur ping...")

class JitterTestStrategy(SpeedTestStrategy):
    def run_test(self):
        print("Mengukur jitter...")

class LatencyTestStrategy(SpeedTestStrategy):
    def run_test(self):
        print("Mengukur latency...")

class SpeedTestContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def run_test(self):
        self._strategy.run_test()

# penggunaan
kecepatan_test_strategy = KecepatanTestStrategy()
ping_test_strategy = PingTestStrategy()
jitter_test_strategy = JitterTestStrategy()
latency_test_strategy = LatencyTestStrategy()

speed_test_context = SpeedTestContext(kecepatan_test_strategy)
speed_test_context.run_test()

speed_test_context = SpeedTestContext(ping_test_strategy)
speed_test_context.run_test()

speed_test_context = SpeedTestContext(jitter_test_strategy)
speed_test_context.run_test()

speed_test_context = SpeedTestContext(latency_test_strategy)
speed_test_context.run_test()

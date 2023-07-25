# pola struktural

class SpeedTest:
    def run_test(self):
        pass

class BaseSpeedTest(SpeedTest):
    def run_test(self):
        print("Mengukur kecepatan internet...")

class SpeedTestDecorator(SpeedTest):
    def __init__(self, speed_test):
        self._speed_test = speed_test

    def run_test(self):
        self._speed_test.run_test()

class PingDecorator(SpeedTestDecorator):
    def run_test(self):
        super().run_test()
        print("Mengukur ping...")

class JitterDecorator(SpeedTestDecorator):
    def run_test(self):
        super().run_test()
        print("Mengukur jitter...")

class LatencyDecorator(SpeedTestDecorator):
    def run_test(self):
        super().run_test()
        print("Mengukur latency...")

# penggunaan
base_speed_test = BaseSpeedTest()
ping_test = PingDecorator(base_speed_test)
jitter_test = JitterDecorator(ping_test)
latency_test = LatencyDecorator(jitter_test)

latency_test.run_test()

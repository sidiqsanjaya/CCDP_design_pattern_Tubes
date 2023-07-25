# pola creational

class SpeedTest:
    def __init__(self):
        self._tests = []

    def add_test(self, test):
        self._tests.append(test)

    def run_tests(self):
        for test in self._tests:
            test.run()

class TestResult:
    def __init__(self):
        self.result = {}

    def add_result(self, test_type, value):
        self.result[test_type] = value

class KecepatanTest:
    def run(self):
        print("Mengukur kecepatan internet...")

class PingTest:
    def run(self):
        print("Mengukur ping...")

class JitterTest:
    def run(self):
        print("Mengukur jitter...")

class LatencyTest:
    def run(self):
        print("Mengukur latency...")

class SpeedTestBuilder:
    def __init__(self):
        self._speed_test = SpeedTest()

    def build_kecepatan_test(self):
        self._speed_test.add_test(KecepatanTest())

    def build_ping_test(self):
        self._speed_test.add_test(PingTest())

    def build_jitter_test(self):
        self._speed_test.add_test(JitterTest())

    def build_latency_test(self):
        self._speed_test.add_test(LatencyTest())

    def get_speed_test(self):
        return self._speed_test

# penggunaan
builder = SpeedTestBuilder()
builder.build_kecepatan_test()
builder.build_ping_test()
builder.build_jitter_test()
builder.build_latency_test()

speed_test = builder.get_speed_test()
speed_test.run_tests()

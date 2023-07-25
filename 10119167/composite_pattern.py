# pola struktural

class SpeedTestComponent:
    def run_test(self):
        pass

class TestGroup(SpeedTestComponent):
    def __init__(self):
        self._tests = []

    def add_test(self, test):
        self._tests.append(test)

    def remove_test(self, test):
        self._tests.remove(test)

    def run_test(self):
        for test in self._tests:
            test.run_test()

class KecepatanTest(SpeedTestComponent):
    def run_test(self):
        print("Mengukur kecepatan internet...")

class PingTest(SpeedTestComponent):
    def run_test(self):
        print("Mengukur ping...")

class JitterTest(SpeedTestComponent):
    def run_test(self):
        print("Mengukur jitter...")

class LatencyTest(SpeedTestComponent):
    def run_test(self):
        print("Mengukur latency...")

# penggunaan
kecepatan_test = KecepatanTest()
ping_test = PingTest()
jitter_test = JitterTest()
latency_test = LatencyTest()

test_group = TestGroup()
test_group.add_test(kecepatan_test)
test_group.add_test(ping_test)
test_group.add_test(jitter_test)
test_group.add_test(latency_test)

test_group.run_test()

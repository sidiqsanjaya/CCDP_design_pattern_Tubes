# pola creational

class SpeedTest:
    def run_test(self):
        pass

class KecepatanTest(SpeedTest):
    def run_test(self):
        print("Mengukur kecepatan internet...")

class PingTest(SpeedTest):
    def run_test(self):
        print("Mengukur ping...")

class JitterTest(SpeedTest):
    def run_test(self):
        print("Mengukur jitter...")

class LatencyTest(SpeedTest):
    def run_test(self):
        print("Mengukur latency...")

class SpeedTestFactory:
    def create_test(self, test_type):
        if test_type == 'kecepatan':
            return KecepatanTest()
        elif test_type == 'ping':
            return PingTest()
        elif test_type == 'jitter':
            return JitterTest()
        elif test_type == 'latency':
            return LatencyTest()

# penggunaan
test_factory = SpeedTestFactory()

tests = ['kecepatan', 'ping', 'jitter', 'latency']
for test_type in tests:
    speed_test = test_factory.create_test(test_type)
    speed_test.run_test()
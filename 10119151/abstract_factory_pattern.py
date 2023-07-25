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
    def create_kecepatan_test(self):
        return KecepatanTest()

    def create_ping_test(self):
        return PingTest()

    def create_jitter_test(self):
        return JitterTest()

    def create_latency_test(self):
        return LatencyTest()

# penggunaan
test_factory = SpeedTestFactory()

speed_test = test_factory.create_kecepatan_test()
speed_test.run_test()

speed_test = test_factory.create_ping_test()
speed_test.run_test()

speed_test = test_factory.create_jitter_test()
speed_test.run_test()

speed_test = test_factory.create_latency_test()
speed_test.run_test()


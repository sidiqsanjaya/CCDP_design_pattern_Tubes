# pola struktural

class KecepatanTest:
    def run_test(self):
        print("Mengukur kecepatan internet...")

class PingTest:
    def run_test(self):
        print("Mengukur ping...")

class JitterTest:
    def run_test(self):
        print("Mengukur jitter...")

class LatencyTest:
    def run_test(self):
        print("Mengukur latency...")

class SpeedTesterFacade:
    def __init__(self):
        self.kecepatan_tester = KecepatanTest()
        self.ping_tester = PingTest()
        self.jitter_tester = JitterTest()
        self.latency_tester = LatencyTest()

    def test_speed(self):
        self.kecepatan_tester.run_test()
        self.ping_tester.run_test()
        self.jitter_tester.run_test()
        self.latency_tester.run_test()

# penggunaan
speed_tester = SpeedTesterFacade()
speed_tester.test_speed()

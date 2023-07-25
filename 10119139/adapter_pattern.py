# pola struktural

class InternetSpeedTester:
    def test_speed(self):
        print("Mengukur kecepatan internet...")

    def test_ping(self):
        print("Mengukur ping...")

    def test_jitter(self):
        print("Mengukur jitter...")

    def test_latency(self):
        print("Mengukur latency...")

class InternetSpeedTestAdapter:
    def __init__(self, internet_speed_tester):
        self.internet_speed_tester = internet_speed_tester

    def run_test(self):
        self.internet_speed_tester.test_speed()

    def run_ping_test(self):
        self.internet_speed_tester.test_ping()

    def run_jitter_test(self):
        self.internet_speed_tester.test_jitter()

    def run_latency_test(self):
        self.internet_speed_tester.test_latency()

class SpeedTest:
    def run_test(self, adapter):
        adapter.run_test()
        adapter.run_ping_test()
        adapter.run_jitter_test()
        adapter.run_latency_test()

# penggunaan
internet_speed_tester = InternetSpeedTester()

speed_test = SpeedTest()

internet_speed_test_adapter = InternetSpeedTestAdapter(internet_speed_tester)
speed_test.run_test(internet_speed_test_adapter)


# pola behavioral

class SpeedTestTemplate:
    def run_test(self):
        self.setup_test()
        self.execute_test()
        self.teardown_test()

    def setup_test(self):
        pass

    def execute_test(self):
        pass

    def teardown_test(self):
        pass

class KecepatanTest(SpeedTestTemplate):
    def setup_test(self):
        print("Menyiapkan pengukuran kecepatan...")

    def execute_test(self):
        print("Mengukur kecepatan internet...")

    def teardown_test(self):
        print("Selesai mengukur kecepatan.")

class PingTest(SpeedTestTemplate):
    def setup_test(self):
        print("Menyiapkan pengukuran ping...")

    def execute_test(self):
        print("Mengukur ping...")

    def teardown_test(self):
        print("Selesai mengukur ping.")

class JitterTest(SpeedTestTemplate):
    def setup_test(self):
        print("Menyiapkan pengukuran jitter...")

    def execute_test(self):
        print("Mengukur jitter...")

    def teardown_test(self):
        print("Selesai mengukur jitter.")

class LatencyTest(SpeedTestTemplate):
    def setup_test(self):
        print("Menyiapkan pengukuran latency...")

    def execute_test(self):
        print("Mengukur latency...")

    def teardown_test(self):
        print("Selesai mengukur latency.")

# penggunaan
kecepatan_test = KecepatanTest()
kecepatan_test.run_test()

ping_test = PingTest()
ping_test.run_test()

jitter_test = JitterTest()
jitter_test.run_test()

latency_test = LatencyTest()
latency_test.run_test()

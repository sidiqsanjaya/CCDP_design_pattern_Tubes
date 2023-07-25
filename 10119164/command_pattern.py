# pola behavioral

class SpeedTestCommand:
    def execute(self):
        pass

class KecepatanTestCommand(SpeedTestCommand):
    def __init__(self, speed_tester):
        self._speed_tester = speed_tester

    def execute(self):
        self._speed_tester.test_kecepatan()

class PingTestCommand(SpeedTestCommand):
    def __init__(self, speed_tester):
        self._speed_tester = speed_tester

    def execute(self):
        self._speed_tester.test_ping()

class JitterTestCommand(SpeedTestCommand):
    def __init__(self, speed_tester):
        self._speed_tester = speed_tester

    def execute(self):
        self._speed_tester.test_jitter()

class LatencyTestCommand(SpeedTestCommand):
    def __init__(self, speed_tester):
        self._speed_tester = speed_tester

    def execute(self):
        self._speed_tester.test_latency()

class InternetSpeedTester:
    def test_kecepatan(self):
        print("Mengukur kecepatan internet...")

    def test_ping(self):
        print("Mengukur ping...")

    def test_jitter(self):
        print("Mengukur jitter...")

    def test_latency(self):
        print("Mengukur latency...")

# penggunaan
internet_speed_tester = InternetSpeedTester()

kecepatan_test_command = KecepatanTestCommand(internet_speed_tester)
ping_test_command = PingTestCommand(internet_speed_tester)
jitter_test_command = JitterTestCommand(internet_speed_tester)
latency_test_command = LatencyTestCommand(internet_speed_tester)

kecepatan_test_command.execute()
ping_test_command.execute()
jitter_test_command.execute()
latency_test_command.execute()

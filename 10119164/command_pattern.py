# pola behavioral

# Penerapan Pola Desain "Command" (Pola Behavioral)

# Kelas SpeedTestCommand merupakan kelas dasar yang mendefinisikan metode execute() sebagai antarmuka untuk semua perintah.
class SpeedTestCommand:
    def execute(self):
        pass

# Kelas-kelas berikut merupakan perintah-perintah konkret yang akan dieksekusi oleh objek InternetSpeedTester.

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

# Kelas InternetSpeedTester bertanggung jawab untuk melakukan pengukuran sesuai dengan jenis perintah yang diberikan.

class InternetSpeedTester:
    def test_kecepatan(self):
        print("Mengukur kecepatan internet...")

    def test_ping(self):
        print("Mengukur ping...")

    def test_jitter(self):
        print("Mengukur jitter...")

    def test_latency(self):
        print("Mengukur latency...")

# Penggunaan Pola Desain "Command" di atas:

# Membuat objek InternetSpeedTester yang akan menerima perintah pengukuran kecepatan internet, ping, jitter, dan latency.
internet_speed_tester = InternetSpeedTester()

# Membuat objek perintah untuk masing-masing jenis pengukuran.
kecepatan_test_command = KecepatanTestCommand(internet_speed_tester)
ping_test_command = PingTestCommand(internet_speed_tester)
jitter_test_command = JitterTestCommand(internet_speed_tester)
latency_test_command = LatencyTestCommand(internet_speed_tester)

# Menjalankan perintah-perintah untuk melakukan pengukuran sesuai dengan jenisnya.
kecepatan_test_command.execute()
ping_test_command.execute()
jitter_test_command.execute()
latency_test_command.execute()

# pola creational

# Penerapan Pola Desain "Builder" (Pola Creational)

# Kelas SpeedTest bertanggung jawab untuk mengatur dan menjalankan serangkaian tes.
class SpeedTest:
    def __init__(self):
        self._tests = []

    def add_test(self, test):
        self._tests.append(test)

    def run_tests(self):
        for test in self._tests:
            test.run()

# Kelas TestResult digunakan untuk menyimpan hasil dari setiap tes yang dijalankan.
class TestResult:
    def __init__(self):
        self.result = {}

    def add_result(self, test_type, value):
        self.result[test_type] = value

# Kelas-kelas berikut merupakan tes-tipe yang akan dijalankan dalam SpeedTest.

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

# Kelas SpeedTestBuilder bertanggung jawab untuk membangun serangkaian tes sesuai dengan kebutuhan.

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

# Penggunaan Pola Desain "Builder" di atas:

# Membuat objek SpeedTestBuilder untuk membangun serangkaian tes.
builder = SpeedTestBuilder()

# Memilih tes-tes yang akan dijalankan dan menambahkannya ke dalam SpeedTest.
builder.build_kecepatan_test()
builder.build_ping_test()
builder.build_jitter_test()
builder.build_latency_test()

# Mendapatkan objek SpeedTest yang sudah dibangun.
speed_test = builder.get_speed_test()

# Menjalankan serangkaian tes yang sudah dibuat.
speed_test.run_tests()

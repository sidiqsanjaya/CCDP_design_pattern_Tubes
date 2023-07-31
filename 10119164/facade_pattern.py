# pola struktural

# Penerapan Pola Desain "Facade" (Pola Struktural)

# Kelas-kelas berikut merepresentasikan tes-tipe yang berbeda dan memiliki fungsi run_test() untuk menjalankan tes.

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

# Kelas SpeedTesterFacade bertindak sebagai facade (antarmuka sederhana) yang menyediakan akses terkoordinasi untuk mengakses tes-tipe.

class SpeedTesterFacade:
    def __init__(self):
        # Inisialisasi objek-objek tes yang akan digunakan dalam facade.
        self.kecepatan_tester = KecepatanTest()
        self.ping_tester = PingTest()
        self.jitter_tester = JitterTest()
        self.latency_tester = LatencyTest()

    def test_speed(self):
        # Memanggil fungsi run_test() untuk menjalankan setiap tes-tipe.
        self.kecepatan_tester.run_test()
        self.ping_tester.run_test()
        self.jitter_tester.run_test()
        self.latency_tester.run_test()

# Penggunaan Pola Desain "Facade" di atas:

# Membuat objek SpeedTesterFacade sebagai antarmuka sederhana untuk mengakses tes-tipe.
speed_tester = SpeedTesterFacade()

# Memanggil fungsi test_speed() pada SpeedTesterFacade untuk menjalankan semua tes-tipe dengan satu perintah.
speed_tester.test_speed()

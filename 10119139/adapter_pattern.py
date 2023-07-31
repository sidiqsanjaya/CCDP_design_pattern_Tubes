# pola struktural

# Definisikan kelas InternetSpeedTester yang bertindak sebagai pengukur kecepatan internet.
# Kode ini hanya mencetak pesan yang menunjukkan bahwa pengukuran sedang berlangsung, tetapi implementasi lebih lanjut dari pengukuran internet sebenarnya akan dilakukan di metode-metode lain.
class InternetSpeedTester:
    def test_speed(self):
        print("Mengukur kecepatan internet...")

    def test_ping(self):
        print("Mengukur ping...")

    def test_jitter(self):
        print("Mengukur jitter...")

    def test_latency(self):
        print("Mengukur latency...")

# Definisikan kelas InternetSpeedTestAdapter yang berfungsi sebagai penghubung antara InternetSpeedTester dan SpeedTest.
# Kita menginisialisasi adapter dengan objek InternetSpeedTester untuk menggunakan fungsionalitasnya.
class InternetSpeedTestAdapter:
    def __init__(self, internet_speed_tester):
        self.internet_speed_tester = internet_speed_tester

    # Jalankan pengujian kecepatan internet menggunakan metode dari objek InternetSpeedTester.
    def run_test(self):
        self.internet_speed_tester.test_speed()

    # Jalankan pengukuran ping menggunakan metode dari objek InternetSpeedTester.
    def run_ping_test(self):
        self.internet_speed_tester.test_ping()

    # Jalankan pengukuran jitter menggunakan metode dari objek InternetSpeedTester.
    def run_jitter_test(self):
        self.internet_speed_tester.test_jitter()

    # Jalankan pengukuran latency menggunakan metode dari objek InternetSpeedTester.
    def run_latency_test(self):
        self.internet_speed_tester.test_latency()

# Definisikan kelas SpeedTest yang berfungsi untuk menjalankan pengujian internet secara keseluruhan.
# Metode run_test menerima objek adapter sebagai argumen dan menjalankan serangkaian pengujian berdasarkan metode-metode adapter tersebut.
class SpeedTest:
    def run_test(self, adapter):
        # Jalankan pengujian kecepatan internet.
        adapter.run_test()
        # Jalankan pengukuran ping.
        adapter.run_ping_test()
        # Jalankan pengukuran jitter.
        adapter.run_jitter_test()
        # Jalankan pengukuran latency.
        adapter.run_latency_test()

# penggunaan
# Membuat objek InternetSpeedTester untuk mengukur kecepatan internet.
internet_speed_tester = InternetSpeedTester()

# Membuat objek SpeedTest untuk menjalankan pengujian internet secara keseluruhan.
speed_test = SpeedTest()

# Membuat objek InternetSpeedTestAdapter dengan menggunakan objek InternetSpeedTester sebagai argumen.
# Hal ini dilakukan agar objek SpeedTest dapat berinteraksi dengan objek InternetSpeedTester walaupun memiliki antarmuka yang berbeda.
internet_speed_test_adapter = InternetSpeedTestAdapter(internet_speed_tester)

# Menjalankan pengujian kecepatan internet dan pengukuran lainnya dengan menggunakan objek SpeedTest.
# Objek InternetSpeedTestAdapter digunakan sebagai argumen untuk melakukan adaptasi antarmuka dengan objek InternetSpeedTester.
speed_test.run_test(internet_speed_test_adapter)



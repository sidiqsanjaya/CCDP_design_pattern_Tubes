# pola creational

# Definisikan kelas SpeedTest sebagai kelas abstrak yang berfungsi sebagai kerangka dasar untuk kelas pengujian lainnya.
# Kelas ini memiliki metode run_test yang tidak diimplementasikan (pass) dan harus diimplementasikan oleh kelas turunannya.
class SpeedTest:
    def run_test(self):
        pass

# Definisikan kelas KecepatanTest yang mewarisi fungsionalitas dari kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur kecepatan internet..." saat dijalankan.
class KecepatanTest(SpeedTest):
    def run_test(self):
        print("Mengukur kecepatan internet...")

# Definisikan kelas PingTest yang mewarisi fungsionalitas dari kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur ping..." saat dijalankan.
class PingTest(SpeedTest):
    def run_test(self):
        print("Mengukur ping...")

# Definisikan kelas JitterTest yang mewarisi fungsionalitas dari kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur jitter..." saat dijalankan.
class JitterTest(SpeedTest):
    def run_test(self):
        print("Mengukur jitter...")

# Definisikan kelas LatencyTest yang mewarisi fungsionalitas dari kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur latency..." saat dijalankan.
class LatencyTest(SpeedTest):
    def run_test(self):
        print("Mengukur latency...")
        
# Definisikan kelas SpeedTestFactory yang bertanggung jawab untuk menciptakan objek pengujian berdasarkan jenis pengujian yang diinginkan.
# Metode-metode create_kecepatan_test, create_ping_test, create_jitter_test, dan create_latency_test
# masing-masing digunakan untuk menciptakan objek pengujian KecepatanTest, PingTest, JitterTest, dan LatencyTest.
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
# Membuat objek SpeedTestFactory yang bertanggung jawab untuk menciptakan objek pengujian berdasarkan jenis pengujian yang diinginkan.
test_factory = SpeedTestFactory()

# Menciptakan objek pengujian KecepatanTest menggunakan SpeedTestFactory.
speed_test = test_factory.create_kecepatan_test()
# Menjalankan pengujian kecepatan internet dengan memanggil metode run_test pada objek pengujian KecepatanTest.
speed_test.run_test()

# Menciptakan objek pengujian PingTest menggunakan SpeedTestFactory.
speed_test = test_factory.create_ping_test()
# Menjalankan pengujian ping dengan memanggil metode run_test pada objek pengujian PingTest.
speed_test.run_test()

# Menciptakan objek pengujian JitterTest menggunakan SpeedTestFactory.
speed_test = test_factory.create_jitter_test()
# Menjalankan pengujian jitter dengan memanggil metode run_test pada objek pengujian JitterTest.
speed_test.run_test()

# Menciptakan objek pengujian LatencyTest menggunakan SpeedTestFactory.
speed_test = test_factory.create_latency_test()
# Menjalankan pengujian latency dengan memanggil metode run_test pada objek pengujian LatencyTest.
speed_test.run_test()



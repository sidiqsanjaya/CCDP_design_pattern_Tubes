# pola creational

# Definisikan kelas SpeedTest yang merupakan kelas abstrak. Kelas ini tidak memiliki implementasi untuk metode run_test.
# Tujuan dari kelas ini adalah untuk menjadi kerangka dasar untuk kelas pengujian lainnya yang akan mewarisi fungsionalitas run_test.
class SpeedTest:
    def run_test(self):
        pass

# Definisikan kelas KecepatanTest yang mewarisi kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test untuk mengukur kecepatan internet.
class KecepatanTest(SpeedTest):
    def run_test(self):
        print("Mengukur kecepatan internet...")

# Definisikan kelas PingTest yang mewarisi kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test untuk mengukur ping.
class PingTest(SpeedTest):
    def run_test(self):
        print("Mengukur ping...")

# Definisikan kelas JitterTest yang mewarisi kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test untuk mengukur jitter.
class JitterTest(SpeedTest):
    def run_test(self):
        print("Mengukur jitter...")

# Definisikan kelas LatencyTest yang mewarisi kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test untuk mengukur latency.
class LatencyTest(SpeedTest):
    def run_test(self):
        print("Mengukur latency...")

# Definisikan kelas SpeedTestFactory yang bertanggung jawab untuk menciptakan objek pengujian berdasarkan tipe pengujian yang diberikan.
# Metode create_test menerima parameter test_type yang menentukan jenis pengujian yang ingin dibuat.
# Kemudian kelas ini mengembalikan objek pengujian yang sesuai berdasarkan tipe yang diberikan.
# Ini adalah contoh pola desain Factory.
class SpeedTestFactory:
    def create_test(self, test_type):
        if test_type == 'kecepatan':
            return KecepatanTest()
        elif test_type == 'ping':
            return PingTest()
        elif test_type == 'jitter':
            return JitterTest()
        elif test_type == 'latency':
            return LatencyTest()

# penggunaan
# Membuat objek SpeedTestFactory yang bertanggung jawab untuk menciptakan objek pengujian berdasarkan tipe pengujian yang diberikan.
test_factory = SpeedTestFactory()

# Daftar pengujian yang ingin dilakukan.
tests = ['kecepatan', 'ping', 'jitter', 'latency']

# Melakukan pengujian untuk setiap tipe pengujian dalam daftar pengujian.
for test_type in tests:
    # Membuat objek pengujian berdasarkan tipe pengujian yang diberikan menggunakan SpeedTestFactory.
    speed_test = test_factory.create_test(test_type)

    # Menjalankan pengujian dengan memanggil metode run_test pada objek pengujian yang telah dibuat.
    speed_test.run_test()

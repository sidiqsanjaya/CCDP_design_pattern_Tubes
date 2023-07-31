# pola behavioral

# Definisikan kelas SpeedTestStrategy sebagai kelas abstrak yang berfungsi sebagai kerangka dasar untuk kelas strategi pengujian lainnya.
# Kelas ini memiliki metode run_test yang tidak diimplementasikan (pass) dan harus diimplementasikan oleh kelas strategi turunannya.
class SpeedTestStrategy:
    def run_test(self):
        pass

# Definisikan kelas KecepatanTestStrategy yang mewarisi fungsionalitas dari kelas SpeedTestStrategy.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur kecepatan internet..." saat dijalankan.
class KecepatanTestStrategy(SpeedTestStrategy):
    def run_test(self):
        print("Mengukur kecepatan internet...")

# Definisikan kelas PingTestStrategy yang mewarisi fungsionalitas dari kelas SpeedTestStrategy.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur ping..." saat dijalankan.
class PingTestStrategy(SpeedTestStrategy):
    def run_test(self):
        print("Mengukur ping...")

# Definisikan kelas JitterTestStrategy yang mewarisi fungsionalitas dari kelas SpeedTestStrategy.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur jitter..." saat dijalankan.
class JitterTestStrategy(SpeedTestStrategy):
    def run_test(self):
        print("Mengukur jitter...")

# Definisikan kelas LatencyTestStrategy yang mewarisi fungsionalitas dari kelas SpeedTestStrategy.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur latency..." saat dijalankan.
class LatencyTestStrategy(SpeedTestStrategy):
    def run_test(self):
        print("Mengukur latency...")

# Definisikan kelas SpeedTestContext yang bertanggung jawab untuk menggunakan sebuah strategi pengujian (SpeedTestStrategy) tertentu.
# Kelas ini memiliki atribut _strategy yang berfungsi sebagai objek strategi pengujian.
# Metode run_test pada kelas ini akan menjalankan metode run_test pada objek strategi pengujian (_strategy).
class SpeedTestContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def run_test(self):
        self._strategy.run_test()

# penggunaan
# Membuat objek KecepatanTestStrategy yang akan menjadi strategi pengujian untuk mengukur kecepatan internet.
kecepatan_test_strategy = KecepatanTestStrategy()

# Membuat objek PingTestStrategy yang akan menjadi strategi pengujian untuk mengukur ping.
ping_test_strategy = PingTestStrategy()

# Membuat objek JitterTestStrategy yang akan menjadi strategi pengujian untuk mengukur jitter.
jitter_test_strategy = JitterTestStrategy()

# Membuat objek LatencyTestStrategy yang akan menjadi strategi pengujian untuk mengukur latency.
latency_test_strategy = LatencyTestStrategy()

# Membuat objek SpeedTestContext dengan menggunakan KecepatanTestStrategy sebagai strategi pengujian.
speed_test_context = SpeedTestContext(kecepatan_test_strategy)
# Menjalankan pengujian kecepatan internet dengan memanggil metode run_test pada objek SpeedTestContext.
speed_test_context.run_test()

# Membuat objek SpeedTestContext dengan menggunakan PingTestStrategy sebagai strategi pengujian.
speed_test_context = SpeedTestContext(ping_test_strategy)
# Menjalankan pengujian ping dengan memanggil metode run_test pada objek SpeedTestContext.
speed_test_context.run_test()

# Membuat objek SpeedTestContext dengan menggunakan JitterTestStrategy sebagai strategi pengujian.
speed_test_context = SpeedTestContext(jitter_test_strategy)
# Menjalankan pengujian jitter dengan memanggil metode run_test pada objek SpeedTestContext.
speed_test_context.run_test()

# Membuat objek SpeedTestContext dengan menggunakan LatencyTestStrategy sebagai strategi pengujian.
speed_test_context = SpeedTestContext(latency_test_strategy)
# Menjalankan pengujian latency dengan memanggil metode run_test pada objek SpeedTestContext.
speed_test_context.run_test()


# pola struktural

# Definisikan kelas SpeedTest sebagai kelas abstrak yang berfungsi sebagai kerangka dasar untuk kelas pengujian lainnya.
# Kelas ini memiliki metode run_test yang tidak diimplementasikan (pass) dan harus diimplementasikan oleh kelas turunannya.
class SpeedTest:
    def run_test(self):
        pass

# Definisikan kelas BaseSpeedTest yang mewarisi fungsionalitas dari kelas SpeedTest.
# Kelas ini mengimplementasikan metode run_test yang mencetak pesan "Mengukur kecepatan internet..." saat dijalankan.
class BaseSpeedTest(SpeedTest):
    def run_test(self):
        print("Mengukur kecepatan internet...")

# Definisikan kelas SpeedTestDecorator yang mewarisi fungsionalitas dari kelas SpeedTest.
# Kelas ini memiliki atribut _speed_test yang berfungsi sebagai objek yang akan didekorasi.
# Metode run_test pada kelas ini akan menjalankan metode run_test pada objek yang didekorasi (_speed_test).
class SpeedTestDecorator(SpeedTest):
    def __init__(self, speed_test):
        self._speed_test = speed_test

    def run_test(self):
        self._speed_test.run_test()

# Definisikan kelas PingDecorator yang mewarisi fungsionalitas dari kelas SpeedTestDecorator.
# Kelas ini mengimplementasikan metode run_test yang memanggil metode run_test pada kelas yang didekorasi, lalu mencetak pesan "Mengukur ping...".
class PingDecorator(SpeedTestDecorator):
    def run_test(self):
        super().run_test()  # Memanggil metode run_test pada kelas yang didekorasi (SpeedTestDecorator).
        print("Mengukur ping...")

# Definisikan kelas JitterDecorator yang mewarisi fungsionalitas dari kelas SpeedTestDecorator.
# Kelas ini mengimplementasikan metode run_test yang memanggil metode run_test pada kelas yang didekorasi, lalu mencetak pesan "Mengukur jitter...".
class JitterDecorator(SpeedTestDecorator):
    def run_test(self):
        super().run_test()  # Memanggil metode run_test pada kelas yang didekorasi (SpeedTestDecorator).
        print("Mengukur jitter...")

# Definisikan kelas LatencyDecorator yang mewarisi fungsionalitas dari kelas SpeedTestDecorator.
# Kelas ini mengimplementasikan metode run_test yang memanggil metode run_test pada kelas yang didekorasi, lalu mencetak pesan "Mengukur latency...".
class LatencyDecorator(SpeedTestDecorator):
    def run_test(self):
        super().run_test()  # Memanggil metode run_test pada kelas yang didekorasi (SpeedTestDecorator).
        print("Mengukur latency...")

# penggunaan
# Membuat objek BaseSpeedTest yang merupakan pengujian dasar untuk mengukur kecepatan internet.
base_speed_test = BaseSpeedTest()

# Membuat objek PingDecorator dengan menggunakan BaseSpeedTest sebagai objek yang akan didekorasi.
# Dengan cara ini, kita menambahkan fitur untuk mengukur ping pada pengujian dasar kecepatan internet.
ping_test = PingDecorator(base_speed_test)

# Membuat objek JitterDecorator dengan menggunakan PingDecorator sebagai objek yang akan didekorasi.
# Dengan cara ini, kita menambahkan fitur untuk mengukur jitter pada pengujian kecepatan internet yang sudah termasuk pengukuran ping.
jitter_test = JitterDecorator(ping_test)

# Membuat objek LatencyDecorator dengan menggunakan JitterDecorator sebagai objek yang akan didekorasi.
# Dengan cara ini, kita menambahkan fitur untuk mengukur latency pada pengujian kecepatan internet yang sudah termasuk pengukuran ping dan jitter.
latency_test = LatencyDecorator(jitter_test)

# Menjalankan pengujian dengan memanggil metode run_test pada objek LatencyDecorator yang sudah memiliki fitur pengukuran kecepatan internet, ping, jitter, dan latency.
latency_test.run_test()


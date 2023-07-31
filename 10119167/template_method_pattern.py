# pola behavioral
# Penerapan Pola Desain "Template Method" (Pola Behavioral)

# Kelas SpeedTestTemplate merupakan kelas abstrak yang mendefinisikan template untuk melakukan tes kecepatan.
# Template method run_test() akan memanggil langkah-langkah yang telah ditentukan, yaitu setup_test(), execute_test(), dan teardown_test().
class SpeedTestTemplate:
    def run_test(self):
        self.setup_test()    # Langkah persiapan sebelum menjalankan tes.
        self.execute_test()  # Langkah eksekusi atau pengukuran.
        self.teardown_test() # Langkah penyelesaian atau pembersihan setelah tes selesai.

    def setup_test(self):
        pass

    def execute_test(self):
        pass

    def teardown_test(self):
        pass

# Kelas-kelas berikut merupakan turunan dari SpeedTestTemplate yang mengimplementasikan langkah-langkah tes spesifik.

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

# Penggunaan Pola Desain "Template Method" di atas:

# Membuat objek-objek tes dengan berbagai jenis.
kecepatan_test = KecepatanTest()
ping_test = PingTest()
jitter_test = JitterTest()
latency_test = LatencyTest()

# Menjalankan tes dengan memanggil metode run_test() pada setiap objek tes.
kecepatan_test.run_test()
ping_test.run_test()
jitter_test.run_test()
latency_test.run_test()

# pola struktural

# Penerapan Pola Desain "Composite"

# Kelas dasar SpeedTestComponent yang berfungsi sebagai kontrak umum bagi semua objek tes.
# Setiap turunan dari SpeedTestComponent wajib mengimplementasikan metode run_test().
class SpeedTestComponent:
    def run_test(self):
        pass

# Kelas TestGroup merupakan turunan dari SpeedTestComponent.
# Kelas ini bertugas untuk mengelola dan menjalankan kumpulan tes yang dimilikinya.
class TestGroup(SpeedTestComponent):
    def __init__(self):
        self._tests = []  # _tests adalah daftar untuk menyimpan tes-tes yang akan dijalankan.

    def add_test(self, test):
        self._tests.append(test)  # Metode untuk menambahkan objek tes ke dalam daftar.

    def remove_test(self, test):
        self._tests.remove(test)  # Metode untuk menghapus objek tes dari daftar.

    def run_test(self):
        # Metode untuk menjalankan semua tes yang ada dalam daftar _tests.
        for test in self._tests:
            test.run_test()

# Kelas-kelas berikut adalah turunan dari SpeedTestComponent.
# Setiap kelas ini merepresentasikan jenis tes tertentu dan harus mengimplementasikan metode run_test().

class KecepatanTest(SpeedTestComponent):
    def run_test(self):
        print("Mengukur kecepatan internet...")

class PingTest(SpeedTestComponent):
    def run_test(self):
        print("Mengukur ping...")

class JitterTest(SpeedTestComponent):
    def run_test(self):
        print("Mengukur jitter...")

class LatencyTest(SpeedTestComponent):
    def run_test(self):
        print("Mengukur latency...")

# Penggunaan Pola Desain "Composite" di atas:

# Membuat objek-objek tes individu.
kecepatan_test = KecepatanTest()
ping_test = PingTest()
jitter_test = JitterTest()
latency_test = LatencyTest()

# Membuat objek TestGroup sebagai wadah untuk menyimpan dan menjalankan tes-tes.
test_group = TestGroup()

# Menambahkan tes-tes individu ke dalam TestGroup.
test_group.add_test(kecepatan_test)
test_group.add_test(ping_test)
test_group.add_test(jitter_test)
test_group.add_test(latency_test)

# Menjalankan semua tes yang ada di dalam TestGroup secara bersamaan.
test_group.run_test()



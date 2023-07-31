# pola creational 
# Penerapan Pola Desain "Prototype" (Pola Creational)

# Kelas dasar SpeedTest merupakan prototipe dasar yang mendefinisikan interface untuk kloning dan menjalankan tes.
class SpeedTest:
    def clone(self):
        pass

    def run_test(self):
        pass

# Kelas-kelas berikut merupakan turunan dari SpeedTest yang mengimplementasikan metode kloning dan menjalankan tes.

class KecepatanTest(SpeedTest):
    def clone(self):
        return copy.copy(self)  # Mengkloning diri sendiri menggunakan copy.copy().

    def run_test(self):
        print("Mengukur kecepatan internet...")

class PingTest(SpeedTest):
    def clone(self):
        return copy.copy(self)

    def run_test(self):
        print("Mengukur ping...")

class JitterTest(SpeedTest):
    def clone(self):
        return copy.copy(self)

    def run_test(self):
        print("Mengukur jitter...")

class LatencyTest(SpeedTest):
    def clone(self):
        return copy.copy(self)

    def run_test(self):
        print("Mengukur latency...")

# Penggunaan Pola Desain "Prototype" di atas:

# Membuat prototipe objek KecepatanTest sebagai objek dasar untuk kloning.
speed_test_prototype = KecepatanTest()

# Mengkloning prototipe objek KecepatanTest untuk membuat beberapa objek tes baru.
test1 = speed_test_prototype.clone()
test2 = speed_test_prototype.clone()
test3 = speed_test_prototype.clone()
test4 = speed_test_prototype.clone()

# Menjalankan tes pada setiap objek yang telah di-klon.
test1.run_test()
test2.run_test()
test3.run_test()
test4.run_test()

# pola behavioral

# Definisikan kelas InternetSpeedSubject sebagai subjek yang melakukan pengukuran kecepatan internet dan memiliki daftar observer yang ingin diberitahu tentang hasil pengukurannya.
class InternetSpeedSubject:
    def __init__(self):
        # Inisialisasi daftar observer sebagai list kosong.
        self._observers = []

    # Metode untuk menambahkan observer baru ke dalam daftar observer.
    def add_observer(self, observer):
        self._observers.append(observer)

    # Metode untuk menghapus observer dari daftar observer.
    def remove_observer(self, observer):
        self._observers.remove(observer)

    # Metode untuk memberitahu semua observer dalam daftar observer tentang perubahan kecepatan internet yang telah diukur.
    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    # Metode untuk mengukur kecepatan internet dan memicu pemanggilan metode update pada semua observer yang terdaftar.
    def test_speed(self):
        print("Mengukur kecepatan internet...")
        # Lakukan pengukuran kecepatan di sini
        self.notify_observers()

    # Metode untuk mengukur ping dan memicu pemanggilan metode update pada semua observer yang terdaftar.
    def test_ping(self):
        print("Mengukur ping...")
        # Lakukan pengukuran ping di sini
        self.notify_observers()

    # Metode untuk mengukur jitter dan memicu pemanggilan metode update pada semua observer yang terdaftar.
    def test_jitter(self):
        print("Mengukur jitter...")
        # Lakukan pengukuran jitter di sini
        self.notify_observers()

    # Metode untuk mengukur latency dan memicu pemanggilan metode update pada semua observer yang terdaftar.
    def test_latency(self):
        print("Mengukur latency...")
        # Lakukan pengukuran latency di sini
        self.notify_observers()

# Definisikan kelas SpeedTestObserver sebagai observer yang akan menerima pembaruan dari InternetSpeedSubject.
class SpeedTestObserver:
    def update(self):
        pass

# Definisikan kelas SpeedTestDisplay sebagai salah satu observer yang menerima pembaruan dari InternetSpeedSubject.
# Kelas ini mengimplementasikan metode update untuk menampilkan hasil pengukuran ke layar.
class SpeedTestDisplay(SpeedTestObserver):
    def update(self):
        print("Menampilkan hasil pengukuran ke layar.")

# Definisikan kelas SpeedTestLogger sebagai salah satu observer yang menerima pembaruan dari InternetSpeedSubject.
# Kelas ini mengimplementasikan metode update untuk mencatat hasil pengukuran ke log file.
class SpeedTestLogger(SpeedTestObserver):
    def update(self):
        print("Mencatat hasil pengukuran ke log file.")


# penggunaan
# Membuat objek InternetSpeedSubject yang bertanggung jawab untuk melakukan pengukuran kecepatan internet dan memiliki daftar observer.
speed_test_subject = InternetSpeedSubject()

# Membuat objek SpeedTestDisplay sebagai observer yang akan menampilkan hasil pengukuran ke layar.
speed_test_display = SpeedTestDisplay()
# Menambahkan observer SpeedTestDisplay ke dalam daftar observer InternetSpeedSubject.
speed_test_subject.add_observer(speed_test_display)

# Membuat objek SpeedTestLogger sebagai observer yang akan mencatat hasil pengukuran ke log file.
speed_test_logger = SpeedTestLogger()
# Menambahkan observer SpeedTestLogger ke dalam daftar observer InternetSpeedSubject.
speed_test_subject.add_observer(speed_test_logger)

# Memulai pengukuran kecepatan internet dan memicu pemanggilan metode update pada semua observer yang terdaftar.
speed_test_subject.test_speed()

# Memulai pengukuran ping dan memicu pemanggilan metode update pada semua observer yang terdaftar.
speed_test_subject.test_ping()

# Memulai pengukuran jitter dan memicu pemanggilan metode update pada semua observer yang terdaftar.
speed_test_subject.test_jitter()

# Memulai pengukuran latency dan memicu pemanggilan metode update pada semua observer yang terdaftar.
speed_test_subject.test_latency()



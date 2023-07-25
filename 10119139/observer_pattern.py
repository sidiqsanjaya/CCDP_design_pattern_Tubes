# pola behavioral

class InternetSpeedSubject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def test_speed(self):
        print("Mengukur kecepatan internet...")
        # Lakukan pengukuran kecepatan di sini
        self.notify_observers()

    def test_ping(self):
        print("Mengukur ping...")
        # Lakukan pengukuran ping di sini
        self.notify_observers()

    def test_jitter(self):
        print("Mengukur jitter...")
        # Lakukan pengukuran jitter di sini
        self.notify_observers()

    def test_latency(self):
        print("Mengukur latency...")
        # Lakukan pengukuran latency di sini
        self.notify_observers()

class SpeedTestObserver:
    def update(self):
        pass

class SpeedTestDisplay(SpeedTestObserver):
    def update(self):
        print("Menampilkan hasil pengukuran ke layar.")

class SpeedTestLogger(SpeedTestObserver):
    def update(self):
        print("Mencatat hasil pengukuran ke log file.")

# penggunaan
speed_test_subject = InternetSpeedSubject()

speed_test_display = SpeedTestDisplay()
speed_test_subject.add_observer(speed_test_display)

speed_test_logger = SpeedTestLogger()
speed_test_subject.add_observer(speed_test_logger)

# Memulai pengukuran kecepatan, ping, jitter, dan latency
speed_test_subject.test_speed()
speed_test_subject.test_ping()
speed_test_subject.test_jitter()
speed_test_subject.test_latency()


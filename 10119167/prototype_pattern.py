# pola creational 

import copy
class SpeedTest:
    def clone(self):
        pass

    def run_test(self):
        pass

class KecepatanTest(SpeedTest):
    def clone(self):
        return copy.copy(self)

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

# penggunaan
speed_test_prototype = KecepatanTest()

test1 = speed_test_prototype.clone()
test2 = speed_test_prototype.clone()
test3 = speed_test_prototype.clone()
test4 = speed_test_prototype.clone()

test1.run_test()
test2.run_test()
test3.run_test()
test4.run_test()

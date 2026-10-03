from threading import Semaphore


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_semaphore = Semaphore(1)
        self.even_semaphore = Semaphore(0)
        self.odd_semaphone = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1):
            self.zero_semaphore.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.odd_semaphone.release()
            else:
                self.even_semaphore.release()

    def even(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(2, self.n + 1, 2):
            self.even_semaphore.acquire()
            printNumber(i)
            self.zero_semaphore.release()

    def odd(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_semaphone.acquire()
            printNumber(i)
            self.zero_semaphore.release()

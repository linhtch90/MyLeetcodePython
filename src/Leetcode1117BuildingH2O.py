from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.hydrogen_semaphore = Semaphore(2)
        self.oxygen_semaphore = Semaphore(1)
        self.barrier = Barrier(3)



    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.hydrogen_semaphore.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.hydrogen_semaphore.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.oxygen_semaphore.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.oxygen_semaphore.release()
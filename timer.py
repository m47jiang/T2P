from threading import Thread

from serveraction import grabfromdatabase, textinfo


class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(5):
            textinfo(grabfromdatabase(""))
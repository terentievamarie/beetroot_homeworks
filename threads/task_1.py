import threading
class Counter(threading.Thread):
    counter = 0
    rounds = 100_000
    def run(self):
        for i in range(self.rounds):
            self.counter+=1
            

t1 = Counter()
t2 = Counter()

t1.start()
t2.start()

t1.join()
t2.join()

print("Final result: ", t1.counter + t2.counter)
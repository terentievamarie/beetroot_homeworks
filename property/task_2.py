class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)

    def get_workers(self):
        return self._workers

    def __str__(self):
        return f"Boss(id={self.id}, name='{self.name}', company='{self.company}')"


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
            new_boss.add_worker(self)

    def __repr__(self):
        return f"Worker(id={self.id}, name='{self.name}', company='{self.company}')"


boss_1 = Boss(1, "Bob", "Apple")
boss_2 = Boss(2, "Erik", "Samsung")

worker_1 = Worker(11, "Alice", "Apple", boss_1)
worker_2 = Worker(14, "John", "Apple", boss_1)

worker_3 = Worker(12, "Alina", "Samsung", boss_2)
worker_4 = Worker(18, "John", "Samsung", boss_2)

print(boss_1.get_workers())
print(boss_2.get_workers())
print(worker_2.boss)

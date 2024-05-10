class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Cola circular llena")
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Cola circular vacía")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

    def get_front(self):
        if self.is_empty():
            raise Exception("Cola circular vacía")
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            raise Exception("Cola circular vacía")
        return self.queue[self.rear]

    def __str__(self):
        return str(self.queue)

# Creamos una cola circular con tamaño máximo de 10 turnos
cola_turnos = CircularQueue(10)

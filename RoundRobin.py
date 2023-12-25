class CircularList:
    def __init__(self, items):
        self.items = items
        self.current_index = 0

    def pop_left(self):
        item = self.items[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.items)
        return item

# Ejemplo de uso
processes = ["P1", "P2", "P3"]
circular_queue = CircularList(processes)

# Pop y recorrido circular
for _ in range(len(processes)):
    print(circular_queue.pop_left())

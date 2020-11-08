class Queue:
    def __init__(self):
        self.elements = []

    def make_queue(self, elements):
        self.elements = [e for e in elements]

    def empty(self):
        return len(self.elements) == 0

    def first(self):
        return self.elements[0] 
    
    def remove_first(self):
        return self.elements.pop(0)

    def insert(self, element):
        self.elements.append(element)
        return self

    def insert_all(self, elements):
        for e in elements:
            self.elements.append(e)
        return self
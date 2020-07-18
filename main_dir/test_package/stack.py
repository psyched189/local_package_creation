class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        a = self.items.pop()
        return a

    def print_stack(self):
        if not self.items:
            print('Stack Empty')
            return
        
        for i in self.items[::-1]:
            print(i)
        print('\n')

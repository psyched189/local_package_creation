class Configuration:
    def __init__(self):
        self.map = {}

    def add(self, key, val):
        self.map[key] = val

    def print_config(self):
        for k, v in self.map.items():
            print(f'{k}:{v}')
            

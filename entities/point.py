class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def print_coordinates(self):
        print(f'({self.x},{self.y})')
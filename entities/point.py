class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def print_coordinates(self):
        print(f'({self.x},{self.y})')
        
    # Point object has knowledge of its hull and segments it belongs to
    # hull is a list of tuples - (p1,p2), where p1p2 is a segment
    def set_hull_details(self, hull_id, tuple_index, is_leftmost):
        self.hull_id = hull_id
        self.tuple_index = tuple_index
        self.is_leftmost: bool = is_leftmost
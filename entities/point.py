class Point:
    # Point is considered "anchor" if it's the point in hull with smallest value of 'x'
    # Point is considered "final" if it's the point in hull with largest value of 'x'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_anchor = False
        self.is_final = False
        
    def print_coordinates(self):
        print(f'({self.x},{self.y})')
        
    # Point object has knowledge of its hull and segments it belongs to
    # hull is a list of tuples - (p1,p2), where p1p2 is a segment
    def set_hull_details(self, hull_id, tuple_index, is_start):
        self.hull_id = hull_id
        if is_start:
            self.starting_index = [tuple_index]
        else:
            self.final_index = [tuple_index]
    
    # If point is anchor, add another index and set its bool to True
    def set_anchor_segment(self, second_index):
        self.is_anchor = True
        self.starting_index.append(second_index)
    
    # If point is final, add another index and set its bool to True
    def set_final_segment(self, second_index):
        self.is_final = True
        self.final_index.append(second_index)
    
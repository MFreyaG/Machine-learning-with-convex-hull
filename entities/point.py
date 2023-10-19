class Point:
    # Point is considered "anchor" if it's the point in hull with smallest value of 'x'
    # Point is considered "final" if it's the point in hull with largest value of 'x'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initialised = False
        self.is_anchor = False
        self.is_final = False
        self.starting_index = []
        self.final_index = []
        
    def print_coordinates(self):
        print(f'({self.x},{self.y})')
        
    # Point object has knowledge of its hull and segments it belongs to
    # hull is a list of tuples - (p1,p2), where p1p2 is a segment
    def set_hull_details(self, hull_id, tuple_index, neighbor_point, is_start):
        self.hull_id = hull_id
        if is_start:
            self.starting_index.append([tuple_index, neighbor_point])
        else:
            self.final_index.append([tuple_index, neighbor_point])
    
    # Point with smaller x value is anchor
    def set_anchor_segment(self, hull_id, first_index, neighbor_point_1, second_index, neighbor_point_2):
        self.hull_id = hull_id
        self.initialised = True
        self.is_anchor = True
        self.starting_index.append([first_index, neighbor_point_1])
        self.starting_index.append([second_index, neighbor_point_2])
    
    # Point with greater smaller x value is anchor
    def set_final_segment(self, hull_id, first_index, neighbor_point_1, second_index, neighbor_point_2):
        self.hull_id = hull_id
        self.initialised = True
        self.is_final = True
        self.final_index.append([first_index, neighbor_point_1])
        self.final_index.append([second_index, neighbor_point_2])
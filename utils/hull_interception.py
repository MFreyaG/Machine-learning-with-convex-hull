from entities.segment import Segment
from entities.point import Point
from entities.avl_tree import AVLTree

from utils.tools import Tools


class HullInterception:
    def _create_hull_segments(self, segments :list[Segment], index_count, hull_id, hull_points: list[Point], ordered_points: list[Point]):
        print(f"Starting hull {hull_id}")
        # Treating the initial point and its peers
        ## "0" is always segment from anchor to next counter clockwise point, "1" is anchor to clockwise next point 
        initial_point = ordered_points[0]
        
        initial_point.set_anchor_segment(hull_id, index_count, hull_points[1], index_count+1, hull_points[-1])
        hull_points[1].set_hull_details(hull_id, index_count, initial_point, 0)
        hull_points[-1].set_hull_details(hull_id, index_count+1, initial_point, 0)
        
        print(f"Adding initial segment {initial_point.x, initial_point.y} -> {hull_points[1].x, hull_points[1].y} @ index {index_count}")
        print(f"Adding initial segment {initial_point.x, initial_point.y} -> {hull_points[-1].x, hull_points[-1].y} @ index {index_count+1}")
        
        segments.append(Segment(initial_point, hull_points[1]))
        segments.append(Segment(initial_point, hull_points[-1]))
        index_count += 2
                
        # Treating final point and its peers
        ## "2" is segment from final point to next clockwise point, "3" is final point to clockwise next point 
        final_point = ordered_points[-1]
        final_point_index = hull_points.index(final_point)
        
        hull_points[final_point_index-1].set_hull_details(hull_id, index_count, final_point, 1)
        print(f"Adding final segment {hull_points[final_point_index-1].x,hull_points[final_point_index-1].y} -> {final_point.x, final_point.y} @ index {index_count}")
        segments.append(Segment(hull_points[final_point_index-1], final_point))
        index_count += 1
        
        if hull_points[-1] != final_point:
            hull_points[final_point_index+1].set_hull_details(hull_id, index_count, final_point, 1)
            final_point.set_final_segment(hull_id, index_count, hull_points[final_point_index-1], index_count+1, hull_points[final_point_index+1])
            print(f"Adding final segment {hull_points[final_point_index+1].x,hull_points[final_point_index+1].y} -> {final_point.x, final_point.y} @ index {index_count}")
            segments.append(Segment(hull_points[final_point_index+1], final_point))
            index_count += 1
        
        # We'll ignore hull starting and final points' segment insertion by checking variable "initialised" in next step!
        
        # Going through other hull points
        for p1, p2 in zip(hull_points, hull_points[1:]):
            both = 0
            if not p1.initialised and not p2.initialised and p2 not in [neighbor[1] for neighbor in p1.starting_index]:
                print(f"Adding start of segment in p1 {p1.x, p1.y} -> {p2.x, p2.y} @ id {index_count}")
                p1.set_hull_details(hull_id, index_count, p2, 1)
                both += 1
            if not p2.initialised and not p1.initialised and p1 not in [neighbor[1] for neighbor in p2.final_index]:
                print(f"Adding end of segment in p2 {p1.x, p1.y} -> {p2.x, p2.y} @ id {index_count}")
                p2.set_hull_details(hull_id, index_count, p1, 0)
                both += 1
            if both == 2:
                print(f"Adding segment {p1.x, p1.y} -> {p2.x, p2.y} @ index {index_count}")
                segments.append(Segment(p1, p2))
            
            if both != 0:
                index_count += 1
    
    def create_hull_segments(self, hull_1, hull_1_orered, hull_2, hull_2_ordered):
        segments = []
        index_count = 0
        
        self._create_hull_segments(segments, index_count, 1, hull_1, hull_1_orered)
        self._create_hull_segments(segments, index_count, 2, hull_2, hull_2_ordered)
        
        return segments
    
    def _check_interception(self, tree :AVLTree, my_segment :Segment, segments):
        tree.insert_node(my_segment)
        
        my_segment_hull = my_segment.smaller.hull_id
                
        # Check predecessor interception
        predecessor = tree.find_predecessor(my_segment)
        if predecessor:
            
            if predecessor.key.smaller.hull_id != my_segment_hull:
                if Tools.do_segments_intercept(my_segment, segments[predecessor.key.smaller.starting_index[0]]):
                    return True
                
        # Check successor interception        
        successor = tree.find_successor(my_segment)
        if successor:
            if successor.key.smaller.hull_id != my_segment_hull:
                if Tools.do_segments_intercept(my_segment, segments[successor.key.smaller.starting_index[0]]):
                    return True
        return False
        
    
    def do_hulls_intercept(self, segments: list[Segment], points: list[Point]):
        tree = AVLTree()
        
        for p in points:
            print(f'Starting point {p.__dict__}')
            # Adding starting segment if p has one
            if not p.is_final:
                print(f'Adding segment: {segments[p.starting_index[0][0]].smaller.x}, {segments[p.starting_index[0][0]].smaller.y} -> {segments[p.starting_index[0][0]].greater.x}, {segments[p.starting_index[0][0]].greater.y}')
          
                if self._check_interception(tree, segments[p.starting_index[0][0]], segments):
                    return True

            # If point is anchor, add 2nd segment. Else, it has a segment we should delete
            if p.is_anchor:
                print(f'Adding segment {segments[p.starting_index[1][0]].smaller.x}, {segments[p.starting_index[1][0]].smaller.y} -> {segments[p.starting_index[1][0]].greater.x}, {segments[p.starting_index[1][0]].greater.y}')      
                
                if self._check_interception(tree, segments[p.starting_index[1][0]], segments):
                    return True
            else:
                print(f'Deleting segment {segments[p.final_index[0][0]].smaller.x}, {segments[p.final_index[0][0]].smaller.y} -> {segments[p.final_index[0][0]].greater.x}, {segments[p.final_index[0][0]].greater.y}')
          
                tree.delete_node(segments[p.final_index[0][0]])
            
            # If point is the final point in hull, also delete 2nd segment
            if p.is_final:
                print(f'Deleting segment {segments[p.final_index[1][0]].smaller.x}, {segments[p.final_index[1][0]].smaller.y} -> {segments[p.final_index[1][0]].greater.x}, {segments[p.final_index[1][0]].greater.y}')
                
                tree.delete_node(segments[p.final_index[1][0]])
            
            print("Printing tree!")
            tree.print_tree()
            print("\n")
                              
        return False
                
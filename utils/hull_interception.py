from entities.segment import Segment
from entities.point import Point
from entities.avl_tree import AVLTree

from utils.tools import Tools


class HullInterception:
    # Gambiarra - mas funciona?
    def _treat_final_point_in_hull(self, my_hull: list[Point], my_hull_id, segments, seg_value):
        hull_rightmost = Tools.find_rightmost_point_in_hull(my_hull)
        rightmost_index = my_hull.index(hull_rightmost)
        
        hull_rightmost.set_hull_details(my_hull_id, seg_value, 0)
        seg_value += 1
        hull_rightmost.set_final_segment(seg_value)
        
        # If rightmost point is last one
        if rightmost_index == len(my_hull)-1:
            segments.append(Segment(my_hull[len(my_hull) - 2], hull_rightmost))
            segments.append(Segment(my_hull[0], hull_rightmost))
            
            # Treat other points
            my_hull[len(my_hull) - 2].set_hull_details(my_hull_id, seg_value-1, 1)
            my_hull[0].set_anchor_segment(seg_value)
        else:
            segments.append(Segment(my_hull[rightmost_index-1], my_hull[rightmost_index]))
            segments.append(Segment(my_hull[rightmost_index+1], my_hull[rightmost_index]))
            
            if my_hull[rightmost_index-1] == my_hull[0]:
                my_hull[0].set_anchor_segment(seg_value-1)
            else:
                my_hull[rightmost_index-1].set_hull_details(my_hull_id, seg_value-1, 1)
            my_hull[rightmost_index+1].set_hull_details(my_hull_id, seg_value, 1)
            
        seg_value += 1
        return rightmost_index, seg_value
    
    
    def _create_hull_segments(self, hull: list[Point], hull_id, seg_value, segments):
        final_index, seg_value = self._treat_final_point_in_hull(hull, hull_id, segments, seg_value)
        
        # Copy hull and remove "final" point
        hull_copy = hull.copy()
        del hull_copy[final_index]
        
        # Go through points
        for p1, p2 in zip(hull_copy, hull_copy[1:]):
            if seg_value not in p1.starting_index:
                p1.set_hull_details(hull_id, seg_value, 1)
            if seg_value not in p2.final_index:
                p2.set_hull_details(hull_id, seg_value, 0)
            
            segments.append(Segment(p1, p2))
            seg_value += 1
            
        # Set initial point, if isn't set
        if not hull[0].is_anchor:
            segments.append(Segment(hull[0], hull[len(hull)-1]))
            hull[0].set_anchor_segment(seg_value)
            
        # Gambiarra - Set last point in hull array as final]
        last_point = hull_copy[len(hull_copy)-1]
        last_point.set_final_segment(hull_copy[0].starting_index[1])
            
        return seg_value
        
    
    # Hull data comes in as [P1,P2,...,Pn], where PiPi+1 is a segment
    def create_hull_segments(self, hull_1: list[Point], hull_2: list[Point]):
        seg_value = 0
        segments = []
        
        seg_value = self._create_hull_segments(hull_1, 1, seg_value, segments)
        seg_value = self._create_hull_segments(hull_2, 2, seg_value, segments)
        
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
                print(f'Adding segment: {segments[p.starting_index[0]].smaller.x}, {segments[p.starting_index[0]].smaller.y} -> {segments[p.starting_index[0]].greater.x}, {segments[p.starting_index[0]].greater.y}')
          
                if self._check_interception(tree, segments[p.starting_index[0]], segments):
                    return True

            # If point is anchor, add 2nd segment. Else, it has a segment we should delete
            if p.is_anchor:
                print(f'Adding segment {segments[p.starting_index[1]].smaller.x}, {segments[p.starting_index[1]].smaller.y} -> {segments[p.starting_index[1]].greater.x}, {segments[p.starting_index[1]].greater.y}')      
                
                if self._check_interception(tree, segments[p.starting_index[1]], segments):
                    return True
            else:
                print(f'Deleting segment {segments[p.final_index[0]].smaller.x}, {segments[p.final_index[0]].smaller.y} -> {segments[p.final_index[0]].greater.x}, {segments[p.final_index[0]].greater.y}')
          
                tree.delete_node(segments[p.final_index[0]])
            
            # If point is the final point in hull, also delete 2nd segment
            if p.is_final:
                print(f'Deleting segment {segments[p.final_index[1]].smaller.x}, {segments[p.final_index[1]].smaller.y} -> {segments[p.final_index[1]].greater.x}, {segments[p.final_index[1]].greater.y}')
                
                tree.delete_node(segments[p.final_index[1]])
            
            print("Printing tree!")
            tree.print_tree()
            print("\n")
                              
        return False
                
from entities.segment import Segment
from entities.point import Point
from entities.avl_tree import AVLTree

from utils.tools import Tools


class HullInterception:
    # Hull data comes in as [P1,P2,...,Pn], where PiPi+1 is a segment - and they're ordered
    def create_hull_segments(self, hull_1, hull_2):
        seg_value = 0
        segments = []
        
        # Going through hull 1
        for p1, p2 in zip(hull_1, hull_1[1:]):
            p1.set_hull_details(1, seg_value, 1)
            p2.set_hull_details(1, seg_value, 0)
            
            segments.append(Segment(p1, p2))
            seg_value += 1
            
        # Adding final segment
        last_hull_1 = hull_1[len(hull_1)-1]

        hull_1[0].set_anchor_segment(seg_value)
        last_hull_1.set_final_segment(seg_value)
        
        segments.append(Segment(hull_1[0], last_hull_1))
        seg_value += 1
            
        # Going thorugh hull 2
        for p1, p2 in zip(hull_2, hull_2[1:]):            
            p1.set_hull_details(2, seg_value, 1)
            p2.set_hull_details(2, seg_value, 0)
            
            segments.append(Segment(p1, p2))
            seg_value += 1
        # Adding final segment
        last_hull_2 = hull_2[len(hull_2)-1]
        
        hull_2[0].set_anchor_segment(seg_value)
        last_hull_2.set_final_segment(seg_value)
        
        segments.append(Segment(hull_2[0], last_hull_2))
        
        seg_value += 1
        
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
        
    
    def do_hulls_intercept(self, segments: list[Segment], points: list[Point]):
        tree = AVLTree()
        
        for p in points:
            # Adding starting segment if p has one
            if not p.is_final:
                if self._check_interception(tree, segments[p.starting_index[0]], segments):
                    return True

            # If point is anchor, add 2nd segment. Else, it has a segment we should delete
            if p.is_anchor:
                if self._check_interception(tree, segments[p.starting_index[1]], segments):
                    return True
            else:
                tree.delete_node(segments[p.final_index[0]])
            
            # If point is the final point in hull, also delete 2nd segment
            if p.is_final:
                tree.delete_node(segments[p.final_index[1]])
                
        return False
                
import bintrees

from tools import Tools
from entities.segment import Segment

class HullInterception:
    # Hull data comes in as [P1,P2,...,Pn], where PiPi+1 is a segment
    @classmethod
    def create_hull_segments(cls, hull_1, hull_2):
        seg_value = 0
        segments = []
        
        # Going through hull 1
        for p1, p2 in zip(hull_1, hull_1[1:]):
            smaller = p1 if p1.x < p2.x else p2
            bigger = p1 if smaller == p2 else p2
            
            smaller.set_hull_details(1, seg_value, 1)
            bigger.set_hull_details(1, seg_value, 0)
            
            segments.append((smaller, bigger))
            seg_value += 1
        
        # Going thorugh hull 2
        for p1, p2 in zip(hull_2, hull_2[1:]):
            smaller = p1 if p1.x < p2.x else p2
            bigger = p1 if smaller == p2 else p2
            
            smaller.set_hull_details(2, seg_value, 1)
            bigger.set_hull_details(2, seg_value, 0)
            
            segments.append(Segment(smaller, bigger))
            seg_value += 1
            
        return segments
    
    
    @classmethod
    def do_hulls_intercept(cls, segments: list, points: list):
        tree = bintrees.RBTree()
        
        for p in points:
            # Find which hull if belongs to
            
            # if point regards left side of segment
            if p.is_leftmost:
                p_segment = segments[p.tuple_index]
                tree.insert(p_segment)
                
                # Should I keep a record of already made comparisons?
                predecessor = tree.find_predecessor(p_segment)
                if predecessor:
                    if predecessor.hull_id != p.hull_id:
                        if Tools.do_segments_intercept(p_segment, segments[predecessor.tuple_index]):
                            return True
                
                # Check successor interception        
                successor = tree.find_successor(p.y)
                if successor:
                    if successor.hull_id != p.hull_id:
                        if Tools.do_segments_intercept(p_segment, segments[successor.tuple_index]):
                            return True
            else:
                # Check if predecessor and successor intercept
                predecessor = tree.find_predecessor(p.y)     
                successor = tree.find_successor(p.y)
                if predecessor and successor and predecessor.hull_id != successor.hull_id:
                    if Tools.do_segments_intercept(
                        segments[predecessor.tuple_index], segments[successor.tuple_index]
                    ):
                        return True
                        
                tree.remove_node(p)
        return False
                
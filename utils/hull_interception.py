from entities.segment import Segment
from entities.avl_tree import AVLTree

from utils.tools import Tools


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
            
            smaller.set_hull_details(1, seg_value)
            
            segments.append(Segment(smaller, bigger))
            seg_value += 1
        # Adding final segment
        last_hull_1 = hull_1[len(hull_1)-1]
        smaller = last_hull_1 if last_hull_1.x < hull_1[0].x else hull_1[0]
        bigger = last_hull_1 if smaller == hull_1[0] else hull_1[0]
        segments.append(Segment(hull_1[0], last_hull_1))
        last_hull_1.set_hull_details(1, seg_value)
        seg_value += 1
            
        # Going thorugh hull 2
        for p1, p2 in zip(hull_2, hull_2[1:]):
            smaller = p1 if p1.x < p2.x else p2
            bigger = p1 if smaller == p2 else p2
            
            smaller.set_hull_details(2, seg_value)
            
            segments.append(Segment(smaller, bigger))
            seg_value += 1
        # Adding final segment
        last_hull_2 = hull_2[len(hull_2)-1]
        smaller = last_hull_2 if last_hull_2.x < hull_2[0].x else hull_2[0]
        bigger = last_hull_2 if smaller == hull_2[0] else hull_2[0]
        segments.append(Segment(smaller, bigger))
        last_hull_2.set_hull_details(2, seg_value)
        seg_value += 1
        
        return segments
    
    
    @classmethod
    def do_hulls_intercept(cls, segments: list, points: list):
        tree = AVLTree()
        
        for p in points:
            p_segment = segments[p.tuple_index]
            # if point regards left side of segment
            if p == p_segment.smaller:
                tree.insert_node(p_segment)
                
                # Should I keep a record of already made comparisons?
                predecessor = tree.find_predecessor(p_segment)
                if predecessor:
                    if predecessor.hull_id != p.hull_id:
                        if Tools.do_segments_intercept(p_segment, segments[predecessor.tuple_index]):
                            return True
                
                # Check successor interception        
                successor = tree.find_successor(p_segment)
                if successor:
                    if successor.hull_id != p.hull_id:
                        if Tools.do_segments_intercept(p_segment, segments[successor.tuple_index]):
                            return True
            else:
                # Check if predecessor and successor intercept
                predecessor = tree.find_predecessor(p_segment)     
                successor = tree.find_successor(p_segment)
                if predecessor and successor and predecessor.hull_id != successor.hull_id:
                    if Tools.do_segments_intercept(
                        segments[predecessor.tuple_index], segments[successor.tuple_index]
                    ):
                        return True
                        
                tree.delete_node(p_segment)
        return False
                
#!/usr/bin/python3
"""
A module for determining if all boxes in a list can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (List[List[int]]): The list of lists representing the boxes and their keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    
    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes.update(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    
    return n == len(seen_boxes)


if __name__ == '__main__':
    main()

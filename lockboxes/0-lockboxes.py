#!/usr/bin/python3

def canUnlockAll(boxes):
    Keys = [0]
    for Key in Keys:
        for n in boxes[Key]:
            if n < len(boxes) and n not in Keys:
                Keys.append(n)
    if len(Keys) == len(boxes):
        return True
    else:
        return False

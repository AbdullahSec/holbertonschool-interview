    # Lockboxes

## Description
This project contains an interview preparation algorithm challenge implemented in Python. The objective is to determine if all locked boxes in a given collection can be opened. 

Each box is numbered sequentially from `0` to `n - 1`, and each box may contain keys to other boxes. The first box (`boxes[0]`) is unlocked by default.

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version 1.7.x)
* All your files must be executable

## Tasks

### 0. Lockboxes
Write a method that determines if all the boxes can be opened.

* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A key with the same number as a box opens that box
* You can assume all keys will be positive integers
* There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`

**File:** `0-lockboxes.py`

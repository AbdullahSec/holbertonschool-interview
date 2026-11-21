# Island Perimeter

The function counts four sides for each land cell. For each shared edge
between adjacent land cells, it removes the two internal sides from the
perimeter. The algorithm runs in O(height * width) time and uses O(1)
additional space.

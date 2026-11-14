class Solution(object):

  def pacificAtlantic(self, heights):
    """:type heights: List[List[int]]

    :rtype: List[List[int]]
    """
    if not heights or not heights[0]:
      return []

    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r, c, visited, prev_height):
      if (
          (r, c) in visited
          or r < 0
          or c < 0
          or r >= rows
          or c >= cols
          or heights[r][c] < prev_height
      ):
        return
      visited.add((r, c))
      for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dfs(r + dr, c + dc, visited, heights[r][c])

    for c in range(cols):
      dfs(0, c, pacific, heights[0][c])
      dfs(rows - 1, c, atlantic, heights[rows - 1][c])

    for r in range(rows):
      dfs(r, 0, pacific, heights[r][0])
      dfs(r, cols - 1, atlantic, heights[r][cols - 1])

    result = list(pacific.intersection(atlantic))
    return result
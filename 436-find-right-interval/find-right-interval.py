from bisect import bisect_left


class Solution(object):

  def findRightInterval(self, intervals):
    """:type intervals: List[List[int]]

    :rtype: List[int]
    """
    n = len(intervals)
    starts = sorted(
        [(interval[0], i) for i, interval in enumerate(intervals)]
    )
    sorted_starts = [item[0] for item in starts]

    res = []
    for interval in intervals:
      end_i = interval[1]
      idx = bisect_left(sorted_starts, end_i)

      if idx < n:
        res.append(starts[idx][1])
      else:
        res.append(-1)

    return res
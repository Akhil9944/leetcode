class SnapshotArray(object):

  def __init__(self, length):
    self.data = [[[0, 0]] for _ in range(length)]
    self.snap_id = 0

  def set(self, index, val):
    if self.data[index][-1][0] == self.snap_id:
      self.data[index][-1][1] = val
    else:
      self.data[index].append([self.snap_id, val])

  def snap(self):
    self.snap_id += 1
    return self.snap_id - 1

  def get(self, index, snap_id):
    history = self.data[index]
    low, high = 0, len(history) - 1
    res_idx = 0
    while low <= high:
      mid = (low + high) // 2
      if history[mid][0] <= snap_id:
        res_idx = mid
        low = mid + 1
      else:
        high = mid - 1
    return history[res_idx][1]
import collections
class TreiNode:
    def __init__(self):
        self.children = collections.defaultdict(TreiNode)

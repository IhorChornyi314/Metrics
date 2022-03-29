import statistics


class Metric:
    """
    Class representing a single metric. Initialized with buffer size.
    To add a datapoint simply use addition operator.
    Also supports item assignment.
    Example:
        from metrics import Metric
        m = Metric(10)
        m += 1
        m += 2
        print(m.mean)
        m[0] = 5
        print(m.median)
    """
    def __init__(self, size=50000):
        self.size = size
        self._list = []

    def __str__(self):
        return str(self._list)

    # override addition operator for ease of use
    def __add__(self, other):
        self._list.append(other)
        if len(self._list) > self.size > 0:
            del self._list[:len(self._list) - self.size]
        return self

    # override getattr to call statistics method instead
    def __getattr__(self, item):
        if not self._list:
            return
        try:
            return statistics.__dict__[item](self._list)
        except KeyError:
            print('No such method found in python statistics module!')

    # Grant access to internal list
    def __getitem__(self, item):
        return self._list[item]

    def __setitem__(self, key, value):
        self._list[key] = value

    def reset(self):
        self._list = []


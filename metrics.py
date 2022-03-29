from metric import Metric


class Metrics:
    """
    A class for collecting and displaying metrics.
    Just declare attributes while initializing the object or create them manually in the code later
    Example:
        from metrics import Metrics, Metric

        m = Metrics('loss', 'reward', size=100)
        m.accuracy = Metric(10)
        m.loss += 10
        m.reward = m.reward + 0 + 5 + -5 + 3
        m.display()
    """
    def __init__(self, *args, size: int, default_aggr='mean'):
        self._default_aggr = default_aggr
        # dynamically create attributes from init arguments
        for arg in args:
            setattr(self, arg, Metric(size))

    def display(self, aggr=None, verbose=True):
        # get aggregate function
        aggr = aggr or self._default_aggr
        # compose result for all user-declared attributes
        result = ''
        for attr in self.__dict__.items():
            if attr[0] == '_default_aggr' or getattr(attr[1], aggr) is None:
                continue
            result += f'{aggr} {attr[0]} value: {getattr(attr[1], aggr)}\n'

        if verbose:
            print(result)
        return result


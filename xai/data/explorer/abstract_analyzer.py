from abc import abstractmethod, ABC
from typing import Iterator
from xai.data.abstract_stats import AbstractStats
class AbstractDataAnalyzer(ABC):

    SUPPORTED_TYPES = []

    @abstractmethod
    def feed(self, value):
        """
        The function feeds one value into analyzer and update the stats object.

        Args:
            value: the value fed into the analyzer for one sample
        """
        raise NotImplementedError('The derived helper needs to implement it.')

    def feed_all(self, values: Iterator):
        """
        The function takes one iterator of values into analyzer and update the stats object.
        Args:
            values: values fed into the analyzer in sequence
        """
        for value in values:
            self.feed(value)

    @abstractmethod
    def get_statistics(self) -> AbstractStats:
        """
        The function returns the up-to-date statistics that the analyzer keeps track
        Returns:
            A Stats jsonobject extends AbstractStats based on data type

        """
        raise NotImplementedError('The derived helper needs to implement it.')

from abc import ABC, abstractmethod

class PositionABC(ABC):

    @abstractmethod
    @property
    def element(self):
        pass

    @abstractmethod
    @property
    def parent(self):
        pass

    # @abstractmethod
    # def __eq__(self, other):
    #     pass
    #
    # @abstractmethod
    # def __ne__(self, other):
    #     pass

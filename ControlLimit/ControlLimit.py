from abc import ABC, abstractmethod

class ControlLimit(ABC):
    def __init__(self, **kwargs):
        self.setup(**kwargs)
        super().__init__()

    @abstractmethod
    def setup(self, **kwargs):
        pass

    @abstractmethod
    def check_sample(self, sample):
        pass

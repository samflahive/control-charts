from abc import ABC, abstractmethod

class ControlCharacteristic(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def accept_sample(self, sample):
        pass


    @abstractmethod
    def get_latest_target_value(self):
        pass

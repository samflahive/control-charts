from .ControlCharacteristic import ControlCharacteristic

class ShewartRangeCharacteristic(ControlCharacteristic):
    def __init__(self):
        super().__init__()

    def accept_sample(self, sample):
        self.sample_range = max(sample) - min(sample)

    def get_latest_target_value(self):
        return self.sample_range

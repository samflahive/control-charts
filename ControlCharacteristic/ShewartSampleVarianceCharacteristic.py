from statistics import variance
from .ControlCharacteristic import ControlCharacteristic

class ShewartSampleVarianceCharacteristic(ControlCharacteristic):
    def __init__(self):
        super().__init__()

    def accept_sample(self, sample):
        self.sample_variance = variance(sample)

    def get_latest_target_value(self):
        return self.sample_deviation

from statistics import stdev
from .ControlCharacteristic import ControlCharacteristic

class ShewartSampleDeviationCharacteristic(ControlCharacteristic):
    def __init__(self):
        super().__init__()

    def accept_sample(self, sample):
        self.sample_deviation = stdev(sample)

    def get_latest_target_value(self):
        return self.sample_deviation

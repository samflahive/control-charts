from .ControlCharacteristic import ControlCharacteristic

class ShewartMeanCharacteristic(ControlCharacteristic):
    def __init__(self):
        super().__init__()

    def accept_sample(self, sample):
        self.sample_mean = sum(sample)/len(sample)

    def get_latest_target_value(self):
        return self.sample_mean

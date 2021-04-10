from .ControlCharacteristic import ControlCharacteristic

class LowerCusumMeanCharacteristic(ControlCharacteristic):
    def __init__(self, target_value, slack, initial_value):
        self.cusum_mean = initial_mean
        self.target = target_value - slack
        super().__init__()

    def accept_sample(self, sample):
        sample_mean = sum(sample)/len(sample)
        target_offset = self.target - sample_mean
        self.cusum_mean = max((0, target_offset + self.cusum_mean))
        

    def get_latest_target_value(self):
        return self.cusum_mean

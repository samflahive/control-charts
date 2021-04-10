from .ControlCharacteristic import ControlCharacteristic

class CusumMeanCharacteristic(ControlCharacteristic):
    def __init__(self, initial_mean, weight_offset):
        self.cusum_mean = initial_mean
        self.weight_offset = weight_offset
        super().__init__()

    def accept_sample(self, sample):
        sample_mean = sum(sample)/len(sample)
        self.cusum_mean += (sample_mean - self.weight_offset)
        

    def get_latest_target_value(self):
        return self.cusum_mean

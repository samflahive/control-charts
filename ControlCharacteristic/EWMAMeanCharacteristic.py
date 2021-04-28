from .ControlCharacteristic import ControlCharacteristic

class EWMAMeanCharacteristic(ControlCharacteristic):
    def __init__(self, initial_mean, weight):
        self.ewma_mean = initial_mean
        self.weight = weight
        super().__init__()

    def accept_sample(self, sample):
        sample_mean = sum(sample)/len(sample)
        self.ewma_mean = (self.weight * sample_mean) + (1- self.weight) * self.ewma_mean
        

    def get_latest_target_value(self):
        return self.ewma_mean

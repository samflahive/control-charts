from .ControlLimit import ControlLimit
    
class DriftControlLimit(ControlLimit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self, **kwargs):
        self.target_mean = kwargs["target_mean"]
        self.sample_count = kwargs["sample_count"]
        
        previous_value = kwargs["previous_value"]
        self.previous_sample_above_target = (previous_value > self.target_mean)
        self.one_side_streak = kwargs["one_sided_streak"]
        

    def check_sample(self, sample):
        sample_above_target = sample >= self.target_mean
        same_side_as_previous = (sample_above_target == self.previous_sample_above_target)
        if same_side_as_previous:
            self.one_side_streak += 1
        else:
            self.one_side_streak = 1
        self.previous_sample_above_target = sample_above_target
        return self.one_side_streak <= self.sample_count


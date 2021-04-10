from .ControlLimit import ControlLimit
    
class LowerControlLimit(ControlLimit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self, **kwargs):
        self.limit = kwargs["limit"]

    def check_sample(self, sample):
        return sample >= self.limit


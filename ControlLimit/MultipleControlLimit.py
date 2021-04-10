from .ControlLimit import ControlLimit

class MultipleControlLimit(ControlLimit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self, **kwargs):
        self.control_limits = kwargs["control_limits"]

    def check_sample(self, sample):
        for limit in self.control_limits:
            if not limit.check_sample(sample):
                return False
        return True

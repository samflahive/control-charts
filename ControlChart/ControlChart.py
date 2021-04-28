class ControlChart:
    def __init__(self, target_value, control_characteristic, control_limits):
        self.control_characteristic = control_characteristic
        self.control_limits = control_limits
        self.control_characteristic_state = None
        self.control_limit_state = True
        self.target_value = target_value

    def accept_sample(self, sample):
        self.control_characteristic.accept_sample(sample)
        self.control_characteristic_state = self.control_characteristic.get_latest_target_value()
        self.control_limit_state = self.control_limits.check_sample(self.control_characteristic_state)

    def get_process_value(self):
        return self.control_characteristic_state

    def check_sample(self, sample):
        self.accept_sample(sample)
        return self.get_limit_state()

    def get_limit_state(self):
        return self.control_limit_state

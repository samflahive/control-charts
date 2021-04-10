from .ControlChart import ControlChart
from .. import ControlCharacteristic
from .. import ControlLimit


def create_ULD_limits(upper_limit, lower_limit, drift_center=0, drift_config=None):
    basic_control_limits = [
                    ControlLimit.UpperControlLimit(limit=upper_limit),
                    ControlLimit.LowerControlLimit(limit=lower_limit)
                    ]
    if drift_config != None:
        basic_control_limits.append(ControlLimit.DriftControlLimit(
            target_mean=drift_config["center"],
            sample_count=drift_config["count_limit"],
            previous_value=drift_config["previous_value"],
            one_sided_streak=drift_config["one_sided_streak"]
            ))
    return ControlLimit.MultipleControlLimit(control_limits=basic_control_limits)


def create_shewart_mean_control_chart(upper_limit, lower_limit, drift_config=None):
    control_characteristic = ControlCharacteristic.ShewartMeanCharacteristic()
    control_limits = create_ULD_limits(
        upper_limit,
        lower_limit,
        drift_config=drift_config
        )
    return ControlChart(control_characteristic=control_characteristic, control_limits=control_limits)

def create_shewart_range_control_chart(upper_limit, lower_limit=0, drift_config=None):
    control_characteristic = ControlCharacteristic.ShewartRangeCharacteristic()
    control_limits = create_ULD_limits(
        upper_limit,
        lower_limit,
        drift_config=drift_config
        )
    return ControlChart(control_characteristic=control_characteristic, control_limits=control_limits)

def create_shewart_deviation_control_chart(upper_limit, lower_limit=0, drift_config=None):
    control_characteristic = ControlCharacteristic.ShewartSampleDeviationCharacteristic()
    control_limits = create_ULD_limits(
        upper_limit,
        lower_limit,
        drift_config=drift_config
        )
    return ControlChart(control_characteristic=control_characteristic, control_limits=control_limits)

def create_shewart_variance_control_chart(upper_limit, lower_limit=0, drift_config=None):
    control_characteristic = ControlCharacteristic.ShewartSampleVarianceCharacteristic()
    control_limits = create_ULD_limits(
        upper_limit,
        lower_limit,
        drift_config=drift_config
        )
    return ControlChart(control_characteristic=control_characteristic, control_limits=control_limits)

def create_cusum_mean_control_chart(initial_mean, weight_offset, upper_limit, lower_limit):
    control_characteristic = ControlCharacteristic.CusumMeanCharacteristic(initial_mean=initial_mean, weight_offset=weight_offset)
    control_limits = create_ULD_limits(
        upper_limit,
        lower_limit
        )
    return ControlChart(control_characteristic=control_characteristic, control_limits=control_limits)

def create_upper_cusum_mean_control_chart(initial_mean, weight_offset, upper_limit, lower_limit):
    control_characteristic = ControlCharacteristic.UpperCusumMeanCharacteristic(initial_mean=initial_mean, weight_offset=weight_offset)
    control_limits = create_ULD_limits(
        upper_limit,
        lower_limit
        )
    return ControlChart(control_characteristic=control_characteristic, control_limits=control_limits)

def create_lower_cusum_mean_control_chart(initial_mean, weight_offset, upper_limit, lower_limit):
    control_characteristic = ControlCharacteristic.LowerCusumMeanCharacteristic(initial_mean=initial_mean, weight_offset=weight_offset)
    control_limits = create_ULD_limits(
        upper_limit,
        lower_limit
        )
    return ControlChart(control_characteristic=control_characteristic, control_limits=control_limits)

def create_ewma_mean_control_chart(initial_mean, weigh, upper_limit, lower_limit):
    control_characteristic = ControlCharacteristic.EWMAMeanCharacteristic(initial_mean=initial_mean, weight=weight)
    control_limits = create_ULD_limits(
        upper_limit,
        lower_limit
        )
    return ControlChart(control_characteristic=control_characteristic, control_limits=control_limits)

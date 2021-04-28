from .CommonControlCharts import *

def create_common_control_chart(
    chart_type,
    target_value,
    previous_value,
    upper_limit,
    lower_limit,
    special_param,
    drift_config):
    """
    drift config = {center, count_limit, previous_value, one_sided_streak}
    """
    # special param = lambda for EWMA and slack for CUSUMs

    if chart_type == "SM":
        return create_shewart_mean_control_chart(target_value, upper_limit, lower_limit, drift_config)
    elif chart_type == "SR":
        return create_shewart_range_control_chart(target_value, upper_limit, lower_limit, drift_config)
    elif chart_type == "SD":
        return create_shewart_deviation_control_chart(target_value, upper_limit, lower_limit, drift_config)
    elif chart_type == "SV":
        return create_shewart_variance_control_chart(target_value, upper_limit, lower_limit, drift_config)
    elif chart_type == "UC":
        return create_upper_cusum_mean_control_chart(target_value, previous_value, special_param, upper_limit, lower_limit)
    elif chart_type == "LC":
        return create_lower_cusum_mean_control_chart(target_value, previous_value, special_param, upper_limit, lower_limit)
    elif chart_type == "EW":
        return create_ewma_mean_control_chart(target_value, previous_value, special_param, upper_limit, lower_limit)
    else:
        raise ValueError("{} is not a known chart type identifier".format(chart_type))


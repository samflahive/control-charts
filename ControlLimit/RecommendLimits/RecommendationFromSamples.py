from statistics import stdev
from .SchewartRecommendations import *

def samples_means(samples):
    xbars = []
    ranges = []
    deviations = []
    for sample in samples:
        sample_mean = sum(sample)/len(sample)
        sample_range = max(sample) - min(sample)
        sample_deviation = stdev(sample)

        xbars.append(sample_mean)
        ranges.append(sample_range)
        deviations.append(sample_deviation)

    xbar_mean = sum(xbars)/len(xbars)
    range_mean = sum(ranges)/len(ranges)
    deviation_mean = sum(deviations)/len(deviations)

    return xbar_mean, range_mean, deviation_mean

def full_recommendations(samples):
    xbar_mean, range_mean, deviation_mean = samples_means(samples)
    sample_size = len(samples[0])
    population_deviation = deviation_mean * (sample_size**0.5)
    
    x_bar_limits = (
        get_xbar_range_upper_lower(xbar_mean, range_mean, sample_size),
        get_xbar_sd_upper_lower(xbar_mean, deviation_mean, sample_size)
        )
    range_limits = (get_range_bar_upper_lower(range_mean, sample_size),)
    deviation_limits = (get_sd_bar_upper_lower(deviation_mean, sample_size),)
    limits = {
        "Process Mean": x_bar_limits,
        "Process Range": range_limits,
        "Process Deviation": deviation_limits
        }
    targets = {
        "Process Mean": xbar_mean,
        "Process Range": range_mean,
        "Process Deviation": deviation_mean
        }
    return {"limits": limits, "targets": targets, "population deviation": population_deviation}

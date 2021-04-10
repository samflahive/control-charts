import sqlite3
import os.path

DATABASE_NAME = "control_lookup.db"
db_name = os.path.dirname(os.path.abspath(__file__)) + "/" + DATABASE_NAME

def validate_sample_size(sample_size):
    if sample_size < 2 or sample_size > 25:
        raise Exception("invalid sample size")

def select_coeff(command, sample_size):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(command, (sample_size,))
    return c.fetchone()[0]

def get_xbar_range_upper_lower(process_mean, range_mean, sample_size):
    validate_sample_size(sample_size)
    command = "SELECT A2 FROM coeffs WHERE sample_size=?"
    A2 = select_coeff(command, sample_size)
    return (process_mean + A2 * range_mean, process_mean - A2 * range_mean)

def get_range_bar_upper_lower(range_mean, sample_size):
    validate_sample_size(sample_size)
    command = "SELECT D4 FROM coeffs WHERE sample_size=?"
    D4 = select_coeff(command, sample_size)
    command = "SELECT D3 FROM coeffs WHERE sample_size=?"
    D3 = select_coeff(command, sample_size)
    return (range_mean*D4, range_mean*D3)

def get_xbar_sd_upper_lower(process_mean, sd_mean, sample_size):
    validate_sample_size(sample_size)
    command = "SELECT A3 FROM coeffs WHERE sample_size=?"
    A3 = select_coeff(command, sample_size)
    return (process_mean + A3 * sd_mean, process_mean - A3 * sd_mean)

def get_sd_bar_upper_lower(sd_mean, sample_size):
    validate_sample_size(sample_size)
    command = "SELECT B4 FROM coeffs WHERE sample_size=?"
    B4 = select_coeff(command, sample_size)
    command = "SELECT B3 FROM coeffs WHERE sample_size=?"
    B3 = select_coeff(command, sample_size)
    return (sd_mean*B4, sd_mean*B3)

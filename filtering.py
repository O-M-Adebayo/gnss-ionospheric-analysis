# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:26:40 2026

@author: user
"""

import numpy as np
from scipy.signal import convolve


def filter_tec_data(tec, lower_minutes, upper_minutes, time_resolution_sec):
    """
    Apply dual moving-average TEC filtering.
    """

    window_1 = int(lower_minutes * 60 / time_resolution_sec)
    window_2 = int(upper_minutes * 60 / time_resolution_sec)

    kernel_1 = np.ones(window_1) / window_1
    kernel_2 = np.ones(window_2) / window_2

    filtered = convolve(tec, kernel_1, mode="same") - \
               convolve(tec, kernel_2, mode="same")

    return filtered

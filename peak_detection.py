# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:27:38 2026

@author: user
"""

import numpy as np


def find_peaks_within_range(data, start_idx, end_idx, threshold, k=1):
    """
    Detect local peaks within index range above threshold.
    """
    peaks = []

    start_idx = max(0, start_idx)
    end_idx = min(len(data), end_idx)

    for i in range(start_idx + k, end_idx - k):
        if data[i] > threshold:
            if data[i] > data[i - k] and data[i] > data[i + k]:
                peaks.append(i)

    return peaks

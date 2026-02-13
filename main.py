# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:28:12 2026

@author: user
"""

import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from geodesy import calculate_distance
from filtering import filter_tec_data
from peak_detection import find_peaks_within_range


def load_tec_file(file_path):
    """
    Load GNSS TEC file and extract relevant columns.
    """
    data = np.loadtxt(file_path)

    return {
        "time": data[:, 1],
        "elevation": np.radians(data[:, 2]),
        "azimuth": np.radians(data[:, 3]),
        "tec": data[:, 4],
    }


def compute_vertical_tec(stec, elevation, earth_radius=6371e3, height=250e3):
    """
    Convert slant TEC to vertical TEC.
    """
    slant_factor = np.cos(
        np.arcsin((earth_radius / (earth_radius + height)) * np.cos(elevation))
    )
    return stec * slant_factor


def process_directory(data_dir, epicenter):
    """
    Process all TEC files in directory.
    """
    file_list = glob.glob(os.path.join(data_dir, "*.dat"))

    results = []

    for file in file_list:
        tec_data = load_tec_file(file)

        stec = tec_data["tec"] - np.min(tec_data["tec"])
        vtec = compute_vertical_tec(stec, tec_data["elevation"])

        results.append({
            "file": os.path.basename(file),
            "max_vtec": np.nanmax(vtec),
            "mean_vtec": np.nanmean(vtec)
        })

    return pd.DataFrame(results)


if __name__ == "__main__":
    DATA_DIRECTORY = "data/"
    EPICENTER = {"lat": -30.4221, "lon": 19.5473}

    df_results = process_directory(DATA_DIRECTORY, EPICENTER)
    print(df_results.head())

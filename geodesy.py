# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:18:47 2026

@author: user
"""

import numpy as np

EARTH_RADIUS_KM = 6371


def calculate_distance(lon1, lat1, lon2, lat2):
    """
    Compute geodesic distance using:
    - Haversine formula
    - Equirectangular approximation

    Returns:
        tuple: (haversine_distance_km, equirectangular_distance_km)
    """
    delta_lat = np.radians(lat2 - lat1)
    delta_lon = np.radians(lon2 - lon1)

    lat1_rad = np.radians(lat1)
    lat2_rad = np.radians(lat2)

    a = (
        np.sin(delta_lat / 2) ** 2
        + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(delta_lon / 2) ** 2
    )

    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    d1 = EARTH_RADIUS_KM * c

    x = delta_lon * np.cos((lat1_rad + lat2_rad) / 2)
    y = delta_lat
    d2 = EARTH_RADIUS_KM * np.sqrt(x**2 + y**2)

    return d1, d2

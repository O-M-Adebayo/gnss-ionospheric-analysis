# GNSS-Based Ionospheric Disturbance Analysis
### DOI: https://doi.org/10.1016/j.jastp.2025.106644

<img width="707" height="302" alt="pids_paper" src="https://github.com/user-attachments/assets/bf46427c-c2bc-492e-9cfa-396b1aad12c0" />

This project processes GNSS-derived Total Electron Content (TEC) data to detect ionospheric disturbances associated with seismic events.

## Overview

The pipeline:

- Parses raw GNSS TEC `.dat` files
- Computes ionospheric piercing points (IPP)
- Calculates epicenter-to-receiver distances
- Applies band-pass filtering and convolution techniques
- Detects TEC perturbations around seismic events
- Visualizes satellite trajectories and dTEC variations

## Key Features

- Haversine-based geodesic distance computation
- Sliding time-window TEC filtering
- Ionospheric piercing point modeling
- Outlier detection and removal
- Signal convolution & band-pass filtering
- Scientific visualization with Matplotlib

## Tech Stack

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib

## Use Case

Designed for ionospheric and space weather analysis, especially investigating GNSS TEC disturbances triggered by earthquakes.

---

## Author
Oluwasegun M. Adebayo  
PhD Research – Ionospheric & GNSS Analysis

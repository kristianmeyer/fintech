#!/usr/bin/env bash

# Create conda environment
conda create -n obb -c conda-forge python=3.10.9 pip pybind11 cmake git cvxpy lightgbm poetry

# Activate the environment
eval "$(conda shell.bash hook)"
conda activate obb

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt


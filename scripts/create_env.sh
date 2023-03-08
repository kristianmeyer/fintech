#!/usr/bin/env bash

conda create -n obb -c conda-forge python=3.10.9 pip pybind11 cmake git cvxpy lightgbm poetry
conda activate obb
pip install "openbb[all]"
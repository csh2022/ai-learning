#!/bin/bash -ex

PYTHON_VERSION=3.9

# install conda manually
# https://docs.anaconda.com/miniconda/

# create conda environment
conda create --name d2l python=$PYTHON_VERSION -y
conda activate d2l

# some packages are not supported by conda, so we install packages with pip
pip install jupyter d2l torch torchvision

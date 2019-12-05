import os

from Cython.Distutils import build_ext
import numpy as np
from setuptools import find_packages
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "README.md"),
          encoding='utf-8') as readme:
    long_description = readme.read()

setup(name="quasildr",
      version="0.1.0",
      long_description=long_description,
      long_description_content_type='text/markdown',
      description=("quasilinear representation methods for single-cell"
                   "omics data"),
      packages=find_packages(),
      url="https://github.com/jzthree/quasildr",
      package_data={
      },
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
      ],
      install_requires=[
        "multiprocess",
        "numpy",
        "pandas",
        "plotly",
        "scikit-learn",
        "scipy",
        "seaborn",
        "statsmodels",
        "plotnine",
        "pynndescent"
    ])
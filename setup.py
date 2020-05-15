#!/usr/bin/env python3

from setuptools import setup

setup(name='OnionPerf',
      version='0.2.pre',
      description='A utility to monitor, measure, analyze, and visualize the performance of Tor and Onion Services',
      author='Rob Jansen',
      url='https://github.com/robgjansen/onionperf/',
      packages=['onionperf'],
      scripts=['onionperf/onionperf'],
      install_requires=["lxml",
                        "matplotlib",
                        "networkx",
                        "nose-cov",
                        "nose",
                        "numpy",
                        "scipy",
                        "stem"]
     )

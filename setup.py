#!/usr/bin/python3
#
#File           :  setup.py
# Author        :  Marcus Zurhorst
#Email          :  marcuszurhorst@gmail.com
# License       :  MIT License
# Copyright     :  (c) 2022 Marcus Zurhorst
#
# Description   :  This module provides functions to gather the hostname, IPv4 address
#                  and upgradeable apt packages and publishs those to an MQTT broker.

from setuptools import setup

setup(name='apt-mqtt-status',
      version='0.0.1',
      description='Small MQTT client, which sends/receives MQTT messages about available APT updates and notifies a Telgram account.',
      url='https: // github.com/mzurhorst/apt-mqtt-status',
      author='Marcus Zurhorst',
      author_email='marcuszurhorst@gmail.com',
      license='GPL',
      packages=['apt-mqtt-status'],
      zip_safe=False)

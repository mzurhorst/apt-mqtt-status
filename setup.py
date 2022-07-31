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

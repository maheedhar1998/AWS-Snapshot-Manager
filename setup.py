from setuptools import setup

setup(
  name='shotty',
  version='0.1',
  author="Maheedhar Mandapati",
  author_email="maheedhar1998@hotmail.com",
  description="Shotty is a AWS EC2 snapshot management tool",
  license="GPLv3+",
  packages=['shotty'],
  url="https://github.com/maheedhar1998/AWS-Snapshot-Manager",
  install_requires=[
    'click',
    'boto3'
  ],
  entry_points="""
    [console_scripts]
    shotty=shotty.shotty:cli
  """,
)

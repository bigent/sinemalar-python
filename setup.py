__author__ = 'bigent'
from setuptools import setup

def local_requirements():
    req_list = []
    with open('requirements.txt') as requirements_file:
        req_list = [line.strip() for line in requirements_file.readlines()]
    install_reqs = list(filter(None, req_list))
    return install_reqs

setup(name='sinemalar',
      version='0.1',
      description='',
      url='https://github.com/bigent/sinemalar-python',
      author='bigent',
      author_email='',
      license='MIT',
      packages=['sinemalar'],
      install_requires=local_requirements(),
      zip_safe=False)
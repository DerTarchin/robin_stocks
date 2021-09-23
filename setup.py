from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(name='robin_stocks',
      version='2.0.3',
      description='A Python wrapper around the Robinhood API',
      long_description='pass',
      long_description_content_type='text/x-rst',
      url='https://github.com/jmfernandes/robin_stocks',
      author='Josh Fernandes',
      author_email='joshfernandes@mac.com',
      keywords=['robinhood','robin stocks','finance app','stocks','options','trading','investing'],
      license='MIT',
      python_requires='>=3',
      packages=find_packages(),
      requires=['requests', 'pyotp'],
      install_requires=[
          'requests',
          'pyotp',
          'python-dotenv'
      ],
      zip_safe=False)

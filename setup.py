#!/usr/bin/env python

import sys
if sys.version_info < (3,0):
    sys.exit('Sorry, Python 3 is required.')

from setuptools import setup

setup(name='Sparkasse+ Exporter',
      version='0.1.0',
      description='Sparkasse+ Exporter exports transaction data from a Sparkasse+ backup file.',
      author='Stefan Siegel',
      author_email='ssiegel@sdas.net',
      url='https://github.com/ssiegel/sparkasse_exporter',
      scripts=['sparkasse-exporter'],
      install_requires=['pysqlcipher3'],
      license='GNU General Public License v3',
     )

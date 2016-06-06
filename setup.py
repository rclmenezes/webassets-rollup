# -*- coding: utf-8 -*-
"""
Rollup filter for webassets
-------------------------------

Filter for for compiling assets using `Rollup <http://rollupjs.org>`_ and
`webassets <http://webassets.readthedocs.org>`_.

Basic usage
```````````

.. code:: python

    from webassets.filter import register_filter
    from webassets_rollup import Rollup

    register_filter(Rollup)


"""
from setuptools import setup, find_packages


setup(name='webassets-rollup',
      version='0.0.1',
      description='Rollup filter for webassets',
      long_description=__doc__,
      author='Rodrigo Menezes',
      license='MIT',
      url='https://github.com/rclmenezes/webassets-rollup',
      packages=find_packages(),
      keywords=['rollup', 'webassets', 'django assets'],
      install_requires=['webassets'],
      test_suite='webassets_rollup.tests',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'
      ])

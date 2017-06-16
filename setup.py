from setuptools import setup
import sys
import os
from setuptools.command.install import install


class Custom(install):
    def run(self):
        print 'Downloading weights for vgg net ....'
        if(not os.path.isfile('/tmp/vgg16_weights.npz')):
            os.system(
                'wget https://www.cs.toronto.edu/~frossard/vgg16/vgg16_weights.npz -P /tmp/ ')
        install.run(self)


setup(name='dvd',
      description='Deep Vision library for Dummies',
      version='0.1.4',
      author='Ajay Prasadh V, Arnav Varma, David Frossard',
      author_email='ajayrfhp1710@gmail.com',
      packages=['dvd'],
      entry_points={
          'console_scripts': ['dvd=dvd:main'],
      },
      cmdclass={
          'install': Custom
      },
      url='https://github.com/ajayrfhp/dvd',
      keywords=['Deep learning', 'Computer Vision',
                'Vision', 'Machine learning'],
      classifiers=[
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities'
      ],
      )

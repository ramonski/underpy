from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()

long_description = read('README.md')

setup(
    name='underpy',
    version='0.1',
    py_modules=['underpy'],
    url='https://github.com/ramonski/underpy',
    license='MIT',
    author='Ramon Bartl',
    author_email='ramon.bartl@googlemail.com',
    tests_require=['nose'],
    description='Functional helpers for Python',
    long_description=long_description,
    platforms='any',
    test_suite='nose.collector',
    classifiers = [
        'Programming Language :: Python :: 2 :: Only',
        'Development Status :: 1 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    setup_requires=['nose>=1.0'],
    extras_require={
      'testing': ['nose'],
    }
)
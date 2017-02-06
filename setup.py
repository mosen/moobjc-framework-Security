'''
Wrappers for the "Security" framework.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="0.1"

setup(
    name='pqobjc-framework-Security',
    description = "Wrappers for the framework Security on Mac OS X",
    min_os_level='10.12',
    packages = [ "Security" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core',
        'pyobjc-framework-Cocoa'
    ],
    long_description=__doc__,
)

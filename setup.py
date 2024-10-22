try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = """
The panda3d-vfs module provides easy access to the virtual file system capabilities of Panda3D
"""

setup(
    name='panda3d_vfs',
    description='Panda3D module provides easy access to the virtual file system capabilities of Panda3D',
    long_description=long_description,
    license='MIT',
    version='1.0.0',
    author='Jordan Maxwell',
    maintainer='Jordan Maxwell',
    url='https://github.com/NxtStudios/panda3d-vfs',
    packages=['panda3d_vfs'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ])

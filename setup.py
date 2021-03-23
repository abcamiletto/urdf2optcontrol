from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Get optimal control from URDF'

# Setting up
setup(
    name="urdf_optcontrol",
    version=VERSION,
    author="Andrea Boscolo Camiletto",
    author_email="<abcamiletto@gmail.com>",
    url="https://github.com/abcamiletto/urdf_optcontrol",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['casadi', 'urdf2casadi', 'numpy', 'matplotlib'],
    keywords=['python', 'optimal_control', 'robotics', 'robots'],
    classifiers=[
        "Topic :: Scientific/Engineering :: Mathematics"
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: Implementation :: CPython"
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
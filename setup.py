from setuptools import find_packages, setup

setup(
    name='snakes_cafe',
    version='2.0.0',
    description='resturant ordering interface',
    long_description='''''',
    url='https://github.com/grandquista/snakes-cafe',
    author='Patricia Raftery, Adam Grandquist',
    author_email='grandquista@gmail.com',
    package_dir={'': 'snakes_cafe'},
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'test': ['pytest'],
    },
)

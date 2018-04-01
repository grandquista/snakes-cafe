from setuptools import setup

setup(
    name='snakes_cafe',
    version='3.0.0',
    description='resturant ordering interface',
    long_description='''''',
    url='https://github.com/grandquista/snakes-cafe',
    author=['Patricia Raftery', 'Adam Grandquist'],
    author_email='grandquista@gmail.com',
    package_dir={'': 'snakes_cafe'},
    install_requires=[],
    extras_require={
        'test': ['pytest'],
    },
)

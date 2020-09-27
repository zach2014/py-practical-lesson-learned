from setuptools import setup

setup(
    name='entry_point_cmd',
    entry_points={
        'console_scripts': [
            'entry_point_cmd = entry_command:main',
        ],
    }
)
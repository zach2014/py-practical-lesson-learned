from setuptools import setup

setup(
    name='entry_point_with_args_cmd',
    entry_points={
        'console_scripts': [
            'entry_point_with_args_cmd=entry_command_with_args:main'
        ]
    }
)
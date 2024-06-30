from setuptools import setup, find_packages

setup(
    name='copy_my_writing',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'copy_my_writing=copy_my_writing.cli:cli',
        ],
    },   
)
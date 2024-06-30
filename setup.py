from setuptools import setup, find_packages

setup(
    name='copy-my-writing',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'Click',
        'langchain',
        'openai',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'copy-my-writing=copy_my_writing.cli:cli',
        ],
    },
)
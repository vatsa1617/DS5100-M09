from setuptools import setup, find_packages

setup(
    name='booklover',
    version='0.1.0',
    author='Srivatsa Balasubramanyam',
    author_email='mhe3sy@virginia.edu',
    description='A package for book lover operations and tests',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    python_requires='>=3.6',
)

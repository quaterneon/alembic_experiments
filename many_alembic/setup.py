from setuptools import find_packages, setup

setup(
    name='schema_test',
    version='2.0',
    description='HTTP web service for training data management',
    author='Agata Kargol',
    author_email='agata@planet.com',
    package_dir={'schema1': 'schema1', 'schema2': 'schema2', 'base': 'base'},
    include_package_data=True,
)

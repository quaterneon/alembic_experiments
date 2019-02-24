from setuptools import find_packages, setup

setup(
    name='schema_test2',
    version='2.0',
    description='HTTP web service for training data management',
    author='Agata Kargol',
    author_email='agata@planet.com',
    package_dir={'schema1_B': 'schema1_B', 'schema2_B': 'schema2_B', 'base_B': 'base_B'},
    include_package_data=True,
)

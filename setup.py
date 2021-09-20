from setuptools import find_packages, setup


setup_requires = ['setuptools']

with open('README.md') as f:
    readme = f.read()

with open('VERSION') as f:
    version = f.read().strip('\n')


setup(
    name='my-py-framework-standards',
    description='Python framework and Standards',
    long_description=readme,
    version=version,
    author='Suvarna K',
    author_email='abc@gmail.com',
    url='https://github.com/SKCodeGen',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyYAML~=5.4',
        'pydantic',
        'pandas',
        'numpy',
        'attrs',
        'flake8',
        'black',
    ],
    setup_requires=setup_requires,  # This should not be required.  There is a warning on pip documentation for not using.
)


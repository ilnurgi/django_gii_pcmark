"""
инсталятор
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name='django_gii_pcmark',
    version='0.0.68',
    author='Ильнур Гайфутдинов',
    author_email='ilnurgi87@gmail.com',
    description='Бенчмарки pc комплектующих',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ilnurgi/django_gii_pcmark/',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
)

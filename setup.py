from setuptools import setup

setup(
    name='vica',
    version='0.1dev',
    packages=['vica'],
    license='All rights reserved, pending review by USDA ARS office of Technology Transfer and Lawrence Berkeley National Laboratory',
    long_description=open('README.rst').read(),
    keywords='virus classifier metagenome RNA DNA microbiome',
    test_suite ='nose.collector',
    #tests_require=['nose'],
    author='Adam R. Rivers, Qingpeng Zhang',
    author_email='adam.rivers@ars.usda.gov',
    install_requires=['tensorflow>=1.3', 'pandas>-0.20.3', 'numpy>=1.13.1', 'biopython>=1.70','scipy>=0.19.0' 'khmer>=2.1.1','ete3', 'pyfaidx>=0.5'],
    tests_require=['nose'],
    include_package_data=True,
    scripts=['vica/get_features.py', 'vica/classifier.py']
    zip_safe=False)

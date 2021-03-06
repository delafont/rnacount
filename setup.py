from setuptools import setup, Extension
import sys

try:
    import numpy as np
except ImportError:
    sys.stderr.write("""\n    Numpy is required for the installation to proceed.
    Please install numpy first (with `sudo easy_install numpy` or `sudo pip install numpy`).\n\n""")
    sys.exit(1)

def readme():
    with open('README.rst') as f:
        return f.read()

ext_modules = [
    Extension("rnacounter/rnacounter", ["rnacounter/rnacounter.c"])
]

setup(name='rnacounter',
    version='1.5.2',
    description='Estimate abundances of genomic features from read densities',
    long_description=readme(),
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Bio-Informatics',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Development Status :: 5 - Production/Stable',
    ],
    keywords='rna-seq rnaseq count reads table sequencing genetics bioinformatics',
    url='https://github.com/delafont/rnacounter',
    author='Julien Delafontaine',
    author_email='julien.delafontaine@epfl.ch',
    license='GPL-2',
    packages=['rnacounter','testfiles'],
    zip_safe=False,
    include_package_data=True,
    package_data={'testfiles':
        ['gapdhKO.bam','gapdhKO.bam.bai','mm9_3genes_renamed.gtf']},
    test_suite='nose.collector',
    install_requires=['numpy','scipy','docopt','nose','pysam','cython'],
    scripts=['bin/rnacounter'],
    cmdclass = {},
    ext_modules = ext_modules,
    include_dirs=[np.get_include()]
)



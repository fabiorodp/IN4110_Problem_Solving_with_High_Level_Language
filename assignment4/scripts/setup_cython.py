from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name="Cython modules",
    ext_modules=cythonize("*.pyx"),
    include_dirs=[numpy.get_include()]
)

"""python setup_cython.py build_ext --inplace"""

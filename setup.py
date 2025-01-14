#!/usr/bin/env python
import os

from setuptools import setup, find_packages


if __name__ == "__main__":

    base_dir = os.path.dirname(__file__)
    src_dir = os.path.join(base_dir, "src")

    about = {}
    with open(os.path.join(src_dir, "fluffy_happiness", "__about__.py")) as f:
        exec(f.read(), about)

    #with open(os.path.join(base_dir, "README.rst")) as f:
    #    long_description = f.read()

    install_requirements = [
        
    ]


    setup(
        name=about['__title__'],
        version=about['__version__'],

        description=about['__summary__'],
        #long_description=long_description,
        #license=about['__license__'],
        url=about["__uri__"],

        author=about["__author__"],
        author_email=about["__email__"],

        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        include_package_data=True,

        install_requires=install_requirements,
        extras_require={
            #'data': data_requires,
        },

        zip_safe=False,

    )

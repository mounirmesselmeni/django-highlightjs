import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-highlightjs',
    version='0.2.4',
    packages=['highlightjs'],
    include_package_data=True,
    license='MIT License',  # example license
    description='A Django app to easy integrate highlight.js syntax highlighter.',
    long_description=README,
    url='https://github.com/MounirMesselmeni/django-highlightjs/',
    author='Mounir Messelmeni',
    author_email='messelmeni.mounir@gmail.com',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

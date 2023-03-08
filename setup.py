"""fintech distutils configuration."""
from setuptools import setup

version = "0.1.0"

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'openbb'
]



setup(
    name='fintech',
    version=version,
    description=(
        'A tool for predicting stocks.'
    ),
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Kristian Meyer',
    author_email='kristianmeyer@icloud.com',
    packages=['fintech'],
    package_dir={'fintech': 'fintech'},
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    keywords=[
        "stocks",
    ],
)
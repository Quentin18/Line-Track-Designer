"""
* Install with pip (recommended):
    pip3 install .
* Install with setuptools:
    python3 setup.py install
* Run tests:
    python3 setup.py pytest
"""
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='line-track-designer',
    version='0.0.1',
    description='A library to design line following tracks for robots',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Quentin Deschamps',
    author_email='quentindeschamps18@gmail.com',
    url='https://github.com/Quentin18/Line-Track-Designer/',
    packages=['line_track_designer'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Education',
        'Topic :: Scientific/Engineering'
    ],
    license='MIT',
    keywords='robotics line follow robot track',
    project_urls={
        'Documentation':
        'https://line-track-designer.readthedocs.io/en/latest/',
        'Travis':
        'https://travis-ci.org/github/Quentin18/Line-Track-Designer/',
        'Source Code': 'https://github.com/Quentin18/Line-Track-Designer/',
    },
    platforms=['any'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['numpy', 'Click', 'Pillow', 'pycups'],
    entry_points='''
        [console_scripts]
        linetrack=line_track_designer.cli:linetrack
    ''',
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require='pytest'
)

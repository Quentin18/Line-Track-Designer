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
    author='Quentin Deschamps',
    author_email='quentindeschamps18@gmail.com',
    description='A library to design line following tracks for robots',
    keywords='line follow robot track',
    license='MIT',
    url='https://github.com/Quentin18/Line-Track-Designer',
    packages=['line_track_designer'],
    platforms='any',
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=['numpy', 'Click'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    setup_requires=['pytest-runner'],
    tests_require='pytest',
    entry_points='''
        [console_scripts]
        linetrack=line_track_designer.cli:linetrack
    '''
)

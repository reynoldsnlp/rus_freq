import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rus_freq',
    version='0.0.1',
    author='Robert Reynolds',
    author_email='ReynoldsRJR@gmail.com',
    description='Russian token- and lemma- frequencies.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/reynoldsnlp/rus_freq',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)

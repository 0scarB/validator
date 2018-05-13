from setuptools import setup


with open('README.md', 'r') as readme:
    README_RAW = readme.read()

setup(
    name="validator",
    version="0.1",
    packages=['validator'],
    package_data={
        '': ['*.md'],
    },
    author="Oscar Butler-Aldridge",
    author_email="oscarb@protonmail.com",
    description=(
        'A validator for strings and parameters in python '
        'with comprehensible error messages'
    ),
    long_description=README_RAW,
    long_description_content_type='text/markdown',
    license='GPLv3',
    keywords='validator validate checker check',
    url='https://github.com/0scarB/validator',
    project_urls={
        'GitHub': 'https://github.com/0scarB/validator',
    },
)

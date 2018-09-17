from setuptools import setup
    
with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='ezi72ulx',
    version='0.0.1',
    author='Allison Parrish',
    author_email='allison@decontextualize.com',
    url='https://github.com/aparrish/ezi72ulx',
    description='Turn Inform 7 code into .ulx files - fast',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    dependency_links=[],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    platforms='any',
)

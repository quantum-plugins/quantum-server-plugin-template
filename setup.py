from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt', 'r') as file:
        lines = list(
                map(lambda line: line.replace('\n','').strip(), file.readlines())
            )
        valid_packages = list(
                filter(lambda line: not line.startswith('#'), lines)
            )
        return valid_packages

def get_long_description():
    with open("README.md", 'r') as file:
        return file.read()

setup(
    name='', # your plugin name
    version='', # your plugin version
    install_requires=get_requirements(),
    packages=find_packages(
        # depending on how you have architected your plugin you may need to update the packages
        # for more info, take a look at: https://setuptools.pypa.io/en/latest/userguide/quickstart.html#package-discovery
       exclude=['[your plugin name].tests']
    ),
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Quantum Computing",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: System",
        "Topic :: System :: Hardware"
    ],
    url='', # your repository url
    license='MIT', 
    author='', # your name
    author_email='', # your dev email
    description='', # describe your plugin
    long_description=get_long_description(), # remember to update the README.md file
    long_description_content_type='text/markdown'
)
# responsible for building and installing your machine learning app as a package
from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = 'e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    the last line is to make sure \n doesn't get added
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]


        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            # it is brought there in the first place to ensure setp.py runs as requirements runs but after then it's no longer needed
            return requirements

setup (

    name='mlproject',
    version='0.0.1',
    author='Aliko',
    author_email='gracealiko08@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
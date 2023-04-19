#build your model as a package so that other can install and use it like an application
from setuptools import find_packages,setup
from typing import List

hypen='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author='Ayush',
    author_email='ayushpsharma88099@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)
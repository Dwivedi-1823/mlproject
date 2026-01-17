from setuptools import  find_packages, setup
from typing import List



H_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This will return list of requirements.
    '''
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if H_E_DOT in requirements:
            requirements.remove(H_E_DOT)
    
    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author='Piyush Dwivedi',
    author_email='piyushdevops1823@outlook.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)
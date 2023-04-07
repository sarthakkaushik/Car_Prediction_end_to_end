from setuptools import find_packages, setup
from typing import List

HYPEH_E_DOT='-e .'
def get_requirments(file_path:str)->list[str]:
    '''
    This function return list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEH_E_DOT in requirements:
                requirements.remove(HYPEH_E_DOT)
    return requirements
        
    

setup(
    
    name='Car_Price_Prediction',
    version='0.0.1',
    author='Sarthak Kaushik',
    author_email='Sarthak.kaushik.17@gmail.com',
    packages=find_packages(), # This function will find all the folder with "__init__.py" and consoder that folder as a package and will try to build this ,and then we can import this (src) like any other packages like pandas and seaborn
    install_requires=get_requirments('requirments.txt')
    
)
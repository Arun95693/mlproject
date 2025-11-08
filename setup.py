# from setuptools import find_packages,setup
# from typing import List

# HYPEN_E_DOT='-e .'
# def get_requirements(file_path:str)->List[str]:
#     '''
#     this function will return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
    
#     return requirements

# setup(
# name='mlproject',
# version='0.0.1',
# author='Arun',
# author_email='231210025@nitdelhi.ac.in',
# packages=find_packages(),
# install_requires=get_requirements('requirements.txt')

# )


from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
DISALLOWED_PREFIXES = ("-r ", "--", "git+", "http://", "https://")

def get_requirements(file_path: str) -> List[str]:
    """
    Return a clean list of install requirement specifiers from requirements.txt.
    Skips editable/local includes, options, comments, and blank lines.
    """
    requirements: List[str] = []
    with open(file_path) as f:
        for raw in f:
            line = raw.strip()  # remove surrounding whitespace & newline
            if not line:                    # skip empty
                continue
            if line.startswith("#"):        # skip comments
                continue
            if line == HYPEN_E_DOT:         # skip editable local install
                continue
            if line.startswith(DISALLOWED_PREFIXES):  # skip includes/options/URLs
                continue
            requirements.append(line)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Arun",
    author_email="231210025@nitdelhi.ac.in",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

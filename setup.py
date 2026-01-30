from setuptools import find_packages, setup



def get_requirements():
    with open("requirements.txt", "r") as file:
        

        return [req.replace("\n", "") for req in file.readlines() if req != "-e ."]
        





setup(

    name="mlProject",
    version="0.0.1",
    author="Mohamad alabbasi",
    description="A machine learning project",
    author_email="mohaammad.akai21@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)
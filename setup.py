from setuptools import find_packages, setup

setup(name="e-commerce-bot",
      version="0.0.1",
      author="Raj",
      author_email="rajendra7427@gmail.com",
      packages=find_packages(),
      install_requires = ['langchain_astradb', 'langchain']
      )

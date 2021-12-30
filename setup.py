import setuptools


setuptools.setup(
    name='data_inspector',
    version='1.0',
    author="Asif Ahmed Neloy",
    author_email="neloyn@myumanitoba.ca",
    description="Data Scaler is an open-source python library to select the appropriate data scaler for your Machine Learning model.",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    License='MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/aaneloy/data-scaler",
    keywords='scaler',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[['pandas==1.2.3','matplotlib==3.1.2','numpy==1.18.5', 'seaborn==0.11.1','scipy==1.6.2']]
)
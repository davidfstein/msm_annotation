from setuptools import setup, find_packages

setup(
    name="msm_annotation",        
    version="0.1.0",                 
    author="David Stein",
    author_email="david.stein@icahn.mssm.edu",
    description="Package for annotating MSM data with VEP",
    packages=find_packages(exclude=["tests*", "docs*"]),
    python_requires=">=3.11",
    install_requires=[
        "python-dotenv",     # specify a minimum if you like
    ],
    entry_points={
        "console_scripts": [
            "annotate_msm = msm_annotation.annotate:main",
        ],
    },
)

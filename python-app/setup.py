from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'calculator=app:main',
        ],
    },
)

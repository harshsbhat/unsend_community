from setuptools import setup, find_packages

setup(
    name="UnsendCommunity",
    version='0.3.0',
    description='An unsend library for Python developers',
    author='Harsh Bhat',
    author_email='harsh121102@gmail.com',
    packages=find_packages(include=['unsendcommunity', 'unsendcommunity.*']),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

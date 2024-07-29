from setuptools import setup, find_packages

setup(
    name="UnsendCommunity",
    version='0.3.2',
    description='A package for sending and managing emails with the Unsend API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
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

from setuptools import setup, find_packages


setup(
    name='base-agent',
    version='0.1.1',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='An abstract base class for building various agent-based systems.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/BaseAgent',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

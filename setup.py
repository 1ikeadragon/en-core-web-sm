from setuptools import setup, find_packages


VERSION = "0.1.0"  # PEP-440

NAME = "en-core-web-sm"



setup(
    name='en-core-web-sm-poc', # Changed package name to be clearly DUMMY
    version=VERSION,
    packages=find_packages(),
    description='Dummy Proof-of-Concept package for supply chain attack demonstration. DO NOT USE.',
    long_description="""
This is a DUMMY package for demonstrating a supply chain attack.
It is NOT a legitimate package and contains NO useful functionality.
It is intentionally designed to be potentially harmful as an example
of what a malicious actor could do.

DO NOT INSTALL OR USE THIS PACKAGE IN ANY PRODUCTION ENVIRONMENT.
IT IS FOR SECURITY RESEARCH AND EDUCATIONAL PURPOSES ONLY.

--- MALICIOUS CODE WARNING ---
This package contains intentionally malicious code to demonstrate
a supply chain takeover scenario.  Running this package could
potentially harm your system or compromise your data (in a real attack,
this code would be designed to do actual harm).

--- END MALICIOUS CODE WARNING ---
""",
    author='Malicious Actor (DUMMY - POC ONLY)',
    author_email='malicious-poc@noskill.agency', # Dummy email
    url='https://example.com/dummy-poc', # Dummy URL
    license='MIT', # Dummy License
    install_requires=[
         'requests',
          'numpy',
    ],
    classifiers=[
        'Development Status :: 1 - Planning', # Dummy status
        'Intended Audience :: Developers', # Dummy audience
        'License :: OSI Approved :: MIT License', # Dummy license
        'Programming Language :: Python :: 3', # Dummy Python version
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    package_data={
        'en_core_web_sm_poc': ['__init__.py'], # Include init - very minimal package
    },
    include_package_data=True,
)

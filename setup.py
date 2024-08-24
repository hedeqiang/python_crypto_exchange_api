from setuptools import setup, find_packages



setup(
    name='crypto_exchange_api',
    version='0.1.5',
    description='A Python framework for accessing multiple cryptocurrency exchanges APIs',
    author='hedeqiang',
    author_email='laravel_code@163.com',
    url='https://github.com/hedeqiang/python_crypto_exchange_api',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

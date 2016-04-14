# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='udon',
    packages=find_packages(exclude=['test']),
    version='0.1.1',
    license='MIT License',
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    description=('Normalizing English lengthened expression having repeating letters.'
                 ' (e.g., "cooooooooooooooollllllllllllll" to "cool")'),
    author='Yukino Ikegami',
    author_email='yukino_0131@me.com',
    url='https://github.com/ikegami-yukino/udon',
    keywords=['normalize', 'lengthened expression', 'English'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Text Processing',
        'Natural Language :: English'
    ],
    long_description='%s\n\n%s' % (open('README.rst', encoding='utf8').read(),
                                   open('CHANGES.rst', encoding='utf8').read())
)

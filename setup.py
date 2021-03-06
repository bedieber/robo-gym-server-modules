import setuptools

setuptools.setup(
    name='robo-gym-server-modules',
    version='0.1.0',
    description='Robot Servers and Server Manager code for robo-gym',
    url='https://github.com/jr-robotics/robo-gym-server-modules',
    author="Matteo Lucchi, Friedemann Zindler",
    author_email="matteo.lucchi@joanneum.at, friedemann.zindler@joanneum.at",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
    'grpcio',
    'protobuf',
    'libtmux'
    ],
    python_requires='>=2.7',
    scripts = [ 'bin/attach-to-server-manager',
                'bin/kill-all-robot-servers',
                'bin/kill-server-manager',
                'bin/start-server-manager'],
)

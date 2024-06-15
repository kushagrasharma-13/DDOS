from setuptools import setup, find_packages

setup(
    name='DDoSDefenseProject',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'scapy',
        'Flask',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'start-dashboard=src.dashboard.app:run',
            'start-sniffer=src.monitoring.packet_sniffer:main',
        ],
    },
)
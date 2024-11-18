from setuptools import find_packages, setup

package_name = 'safety_node'

setup(
    name=package_name,
    version='0.0.1',  # Increment the version
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'sensor_msgs', 'nav_msgs', 'ackermann_msgs'],
    zip_safe=True,
    maintainer='ubuntu22',
    maintainer_email='ubuntu22@todo.todo',
    description='Automatic Emergency Braking Node for F1TENTH',
    license='MIT',  # Update with your license if applicable
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aeb_node = safety_node.aeb_node:main',  # Add the entry point for your node
        ],
    },
)


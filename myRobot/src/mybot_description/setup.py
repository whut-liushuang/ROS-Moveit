from setuptools import setup

from glob import glob #这里
import os #这里

package_name = 'mybot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/**')), #这里
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yong',
    maintainer_email='yong@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

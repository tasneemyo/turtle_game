from setuptools import find_packages, setup

package_name = 'my_robot_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tasneem',
    maintainer_email='tasneem@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node=my_robot_control.first_node:main",
            "draw_circle=my_robot_control.draw_circle:main",
            "pose_sub=my_robot_control.pose_sub:main",
            "turtle_control=my_robot_control.turtle_control:main",
            "random=my_robot_control.random:main",
            "kill=my_robot_control.kill:main",
            "location=my_robot_control.location:main",
            "move=my_robot_control.move:main",
            "talker=my_robot_control.talker:main",
            "listener=my_robot_control.listener:main"
        ],
    },
)

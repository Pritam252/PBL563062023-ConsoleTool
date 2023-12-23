from setuptools import setup

setup(
    name='pbl-console-tool-563062023',
    version='0.1.0',    
    description='Console based Administration tool for the PBL563062023 Project.',
    url='https://github.com/Pritam252/PBL563062023-ConsoleTool',
    author='Pritam252',
    author_email='pritampradhan254@gmail.com',
    license='MIT',
    packages=['pblconsoletool'],
    install_requires=['requests'                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research :: PBL',
        'License :: OSI Approved :: MIT',  
        'Operating System :: Windows :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points = {
        'console_scripts': ['pbl306-console-tool=pblconsoletool.cmdline:main']
    },
)
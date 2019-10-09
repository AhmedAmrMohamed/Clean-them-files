import setuptools

setuptools.setup(
        name="Clean them files",
        version="1",
        author="theunderdog",
        author_email="ahmedbonumstelio@gmail.com",
        url="https://github.com/theunderd0g/Clean-them-files",
        packages=setuptools.find_packages(),
        classifiers=[
        "Programmin Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
        entry_points = {
            'console_scripts' : ['ctf=src.command:main']
            }
        )

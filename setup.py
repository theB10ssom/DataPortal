import setuptools

setuptools.setup(
    name="dataportal",
    version="1.0",
    license='MIT',
    author="Yongmin",
    author_email="jhk3211@icloud.com",
    description="공공데이터포털 api 다운로드",
    #long_description=open('README.md').read(),
    #url="github url 등",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "pandas>=1.*",
        "xmltodict>=0.12.0",
        "requests>=2.25.1,
        "urllib3>=1.26.4",
    ]
)
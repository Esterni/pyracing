import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyracing_bullethell',
    version='0.1.3',
    author='Jacob Anderson & Xander Riga',
    description='A complete overhaul of ir_webstats; pyracing is an API '
                'wrapper for simracing service "iRacing" that queries known '
                'URL endpoints and returns JSON data that is accessible '
                'through objects instead of dictionaries.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bULLETHELL/pyracing.git',
    project_urls={
        "Documentation": "https://esterni.github.io/pyracing/"
    },
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    install_requires=['httpx>=0.13.3,<0.14']
)

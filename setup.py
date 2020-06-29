import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='ir_webstats_rc',
      version='1.3.2',
      author='Rob Crouch',
      author_email='rob.crouch@gmail.com',
      description='A version of ir_webstats hacked on by Rob Crouch',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/fuzzwah/ir_webstats_rc',
      packages=setuptools.find_packages(),
      python_requires='>=3.6',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      zip_safe=False)

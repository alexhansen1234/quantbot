import setuptools

setuptools.setup(
    name="quantlib",
    version="0.1",
    description='code lib for quant stuff',
    url="#",
    author="Me",
    install_requires=[
        # "scikit-build",
        # "opencv-python",
        "yfinance",
        "pandas",
        "beautifulsoup4"
    ],
    author_email="",
    packages=setuptools.find_packages(),
    zip_safe=False
)

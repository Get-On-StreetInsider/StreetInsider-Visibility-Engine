from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="streetinsider-visibility-engine",
    version="1.0.0",
    author="GetOnStreetInsider.com",
    author_email="info@getonstreetinsider.com",
    description="StreetInsider Visibility Engine is a lightweight content visibility and publication workflow tool designed to help businesses, brands, and publishers organize, optimize, and monitor their media content for greater online discoverability.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://getonstreetinsider.com",
    project_urls={
        "Homepage": "https://getonstreetinsider.com",
        "GitHub": "https://github.com/GetOnStreetInsider/StreetInsider-Visibility-Engine",
        "Documentation": "https://streetinsider-visibility-engine.readthedocs.io",
        "PyPI": "https://pypi.org/project/streetinsider-visibility-engine",
    },
    py_modules=["visibility_engine"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords=[
        "streetinsider",
        "visibility-engine",
        "content-visibility",
        "publication-workflow",
        "press-release",
        "media-distribution",
        "metadata-validation",
        "ai-discoverability",
    ],
    entry_points={
        "console_scripts": [
            "streetinsider-engine=visibility_engine:main",
        ],
    },
)

from setuptools import setup, find_packages

setup(
    name="defconfig_explainer",
    version="0.1.0",
    description="A tool to analyze and explain Kconfig defconfig files.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Ichiro Kawazome",
    author_email="ichiro_k@ca2.so-net.ne.jp",
    url="https://github.com/ikwzm/defconfig_explainer",
    packages=find_packages(),
    py_modules=["defconfig_explainer"],
    entry_points={
        "console_scripts": [
            "defconfig-explainer=defconfig_explainer:main",
        ],
    },
    install_requires=[
        "kconfiglib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD-2-Clause",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

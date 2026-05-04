from setuptools import setup, find_packages

setup(
    name="credential-proxy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["cryptography"],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "credential-proxy=credential_proxy.cli:main",
        ],
    },
)

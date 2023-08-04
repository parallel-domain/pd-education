from setuptools import find_packages, setup

setup(
    name="pd_education",
    version="0.1.0",
    author=", ".join(["Nate Cibik"]),
    author_email=", ".join(
        [
            "nate@paralleldomain.com"
        ]
    ),
    packages=find_packages(),
    python_requires=">=3.8",
    long_description="Package for onboarding users to Parallel Domain systems.",
    install_requires=[
        "paralleldomain @ git+ssh://git@github.com/parallel-domain/pd-sdk-internal@nate/rerun-notebook-compat",
        "pd-api-py @ git+ssh://git@github.com/parallel-domain/pd-api-py-internal@main",
        "rerun-sdk>=0.7.0",
        "py7zr>=0.20.5,<1.0.0",
        "filelock>=3.0.0,<4.0.0",
        "matplotlib>=3.7.1,<4.0.0",
        "pandas>=1.3.5,<2.0.0",
        "watchdog>=3.0.0,<4.0.0",
        "dash-core-components>=2.0.0",
        "dash>=2.9.3",
        "imgui[glfw]>=2.0",
        "jupyter-dash>=0.4.2",
        "nbformat>=5.0.0",
        "jupyter",
        "opensimplex",
    ],
    include_package_data=True,
    extras_require={
        "dev": [
            "pre-commit>=2.13.0,<3.0.0",
        ],
    },
    zip_safe=False,
)

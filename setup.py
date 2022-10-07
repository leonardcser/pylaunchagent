from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


def requirements():
    with open("requirements/requirements.txt") as f:
        return list(f.readlines())


setup(
    name="pylaunchagent",
    version="0.0.1",
    description="Install Python code to macOS LaunchAgents",
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requirements(),
    url="https://github.com/leonardcser/pylaunchagent",
    author="Leonard C.",
    classifiers=[],
    scripts=[
        "scripts/pylaunchagent",
        "scripts/pylaunchagent_install_venv",
        "scripts/pylaunchagent_run",
    ],
)

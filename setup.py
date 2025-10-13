from setuptools import setup, find_packages

setup(
    name="study_reminders",
    version="1.0",
    author="Storm O",
    description="A Python package for sending personalized study reminders to students, so they can do their damned work on time.",
    packages=find_packages(),
    install_requires=["schedule"],
    python_requires=">=3.8",
)
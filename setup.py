from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = "discord_user.py",
    version = "1.0.0",
    url = "https://github.com/Zakovskiy/discord_user.py",
    download_url = "https://github.com/Zakovskiy/discord_user.py/tarball/master",
    license = "MIT",
    author = "Zakovskiy",
    author_email = "gogrugu@gmail.com",
    description = "A library to create Discord User bots.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = [
        "discord",
        "user",
        "discord.py",
        "discord_user.py",
        "discord-bot",
        "api",
        "python",
        "zakovskiy",
        "official"
    ],
    install_requires = [
        "setuptools",
        "requests",
    ],
    setup_requires = [
        "wheel"
    ],
    packages = find_packages()
)
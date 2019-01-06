import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GenericTictactoe",
    version="1.1.0",
    author="Anil Battalahalli",
    author_email="anilbattalahalli@gmail.com",
    description="A Generic NxN TicTacToe Library",
    url="https://github.com/AnilBattalahalli/tic-tac-toe/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)


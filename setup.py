import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="g_tictactoe",
    version="1.0.1",
    author="Anil Battalahalli",
    author_email="anil.battalahalli@gmail.com",
    description="A Generic NxN TicTacToe Library",
    url="https://github.com/AnilBattalahalli/tic-tac-toe/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)


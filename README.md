# Intro To Python

## SWBATs

- Print to the terminal using the `print()` function.
- Use the correct naming convention to create and use variables.
- Identify the common data types in Python `str`, `int`, `float`, `bool`, `list`, `tuple`, `set`, `dict`, `None`.
- Create and invoke functions in python.
- Use the `ipdb` library to debug Python code.
- Use comparison operators in Python
- Use Logical operators in Python
- Use `for` and `while` loops in Python
- Use List Comprehensions in Python

## Installing Python

- Mac
    
    ## **Install pyenv**
    
    Before installing Python, we first need to install `pyenv`, a version manager for Python. We will likely only use Python version for our last two workshops, but installing `pyenv` will make it simple to install newer versions later on.
    
    Enter the following command in the Terminal:
    
    ```bash
    brew install pyenv
    ```
    
    Open your shell startup file (either `.zshrc` or `.bash_profile`) with the following command:
    
    ```bash
    code ~/.zshrc
    ```
    
    or
    
    ```bash
    code ~/.bash_profile
    ```
    
    Add the following to the end of the file:
    
    ```bash
    if which pyenv > /dev/null; then 
      eval "$(pyenv init -)";
    fi
    ```
    
    We want to load `pyenv` every time we open a new terminal window; this will make sure that it does! Enter the following command to load your new settings:
    
    ```bash
    source ~/.zshrc
    ```
    
    or
    
    ```bash
    source ~/.bash_profile
    ```
    
    ---
    
    ## **Install Python**
    
    Run the following command to install Python (you'll notice pyenv makes us put in the exact version instead of being able to just say 3.8 or 3):
    
    ```bash
    pyenv install 3.8.13
    ```
    
    After some time this should complete without any errors. It could take a while since you are compiling Python from source code.
    
    Once this is finished we also need to tell pyenv this is our default version of Python using this command:
    
    ```bash
    pyenv global 3.8.13
    ```
    
    Ensure that these changes take effect by closing your terminal and opening a new one.
    
    ### **Check Your Work**
    
    You can verify that you have the correct version of Python installed by typing:
    
    ```bash
    python3 --version
    ```
    
    This command should show 3.8.13.
    
    ---
    
    ## **Install Pipenv**
    
    Another piece of software we will use in class is Pipenv. We will learn more about what Pipenv is later; for now, go ahead and install it:
    
    ```bash
    pip install pipenv
    ```
    
    After you have installed pipenv, modify your shell startup file (either `~/.zshrc` or `~/.bash_profile`) to add an export line inside the `if` statement we added earlier, after the `eval` line:
    
    ```bash
     if which pyenv > /dev/null; then
         eval "$(pyenv init - )";
         export PIPENV_VENV_IN_PROJECT=1
     fi
    ```
    
    Save and close your shell startup file, then enter the following command once again to finish configuring your environment:
    
    ```bash
    source ~/.zshrc
    ```
    
    or
    
    ```bash
    source ~/.bash_profile
    ```
    
    Congratulations! If you've completed all these steps you are ready to code in Python!
    
    ---
    
- Windows
    
    ## **Install pyenv**
    
    Before installing Python, we need to install the Python version manager `pyenv`. This is similar to the nvm tool we used to install Node.JS, except it controls which versions of Python we use on our system.
    
    To install `pyenv`, we use the [pyenv-installer.](https://github.com/pyenv/pyenv-installer)
    
    Per the instructions on the [pyenv-installer](https://github.com/pyenv/pyenv-installer) website, we start by running the following command:
    
    ```bash
    curl https://pyenv.run | bash
    ```
    
    Unlike nvm, `pyenv` does not automatically add its startup lines to your shell startup file.
    
    The files that you have to change will depend on which shell you are running (you can check which shell you have by running echo $SHELL). Follow the instructions to update the startup files associated with the shell that you are running.
    
    Open your `.zshrc` or `.bashrc` file with the following command:
    
    ```bash
    code ~/.zshrc
    ```
    
    or
    
    ```bash
    code ~/.bashrc
    ```
    
    Add the following lines:
    
    ```bash
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"
    ```
    
    To get your startup file to execute, restart your terminal.
    
    ---
    
    ## **Installing Dependencies on Windows and Ubuntu**
    
    For Windows and Ubuntu users you will need to install some extra dependencies for Python. (See here for more information about the prerequisites: pyenv Prerequisites)
    
    First run this command to update your apt repositories:
    
    ```bash
    sudo apt update
    ```
    
    Next, run this command to install the packages listed on the `pyenv`:
    
    ```bash
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
    ```
    
    ## **Installing Python**
    
    Run the following command to install Python (you'll notice `pyenv` makes us put in the exact version instead of being able to just say 3.8 or 3):
    
    ```bash
    pyenv install 3.8.13
    ```
    
    After some time this should complete without any errors. It could take a while since you are compiling Python from source code.
    
    Once this is finished we also need to tell `pyenv` this is our default version of Python using this command:
    
    ```bash
    pyenv global 3.8.13
    ```
    
    Ensure that these changes take effect by closing your terminal and opening a new one.
    
    ### **Checking Your Work**
    
    You can verify that you have the correct version of Python installed by typing:
    
    ```bash
    python --version 
    python3 --version
    ```
    
    Both of these commands should show 3.8.13
    
    ---
    
    ## **Installing Pipenv**
    
    Another piece of software we will use in class is Pipenv. We will learn more about what Pipenv is later; for now, go ahead and install it:
    
    `$ pip install pipenv`
    
    After you have installed pipenv, modify your shell startup file (either `~/.bash_profile` or `~/.zshrc`) to add an export line. This should go somewhere after the `eval "$(pyenv init -)"`:
    
    `$ export PIPENV_VENV_IN_PROJECT=1`
    
    Congratulations! If you've completed all these steps you are ready to code in Python!
    

## What is Python?

[https://www.w3schools.com/python/python_intro.asp](https://www.w3schools.com/python/python_intro.asp)

## The Print function

Similar to the `console.log` method in JavaScript, the Python `print()` function is used to print the specified message to the screen, or other standard output device.

The message can be a string, or any other object, the object will be converted into a string before written to the screen.

## Common Data Types in Python

[https://www.w3schools.com/python/python_datatypes.asp](https://www.w3schools.com/python/python_datatypes.asp)

- **String (constructor: str())** - The `str` type in Python is similar to the JS String data type. They are defined using single or double quotes only - **no back tics in Python**.
    - For string interpolation, we use the f-string:
    
    ```python
    place_of_interest = "world"
    greeting = f"Hello, {place_of_interest}"
    ```
    
- **Integers (constructor: int())** and **Floats (constructor: float())** - Like Ruby, Python will consider any number written without decimals as an `int` (as in 138) and any number written with decimals as a `float` (as in 138.0)
- **Boolean** - `True` and `False` (True and False need to be capitalized)
- **List (constructor: list()) -** Comparable to the Ruby array, a `list` in Python is any set of comma separated data enclosed in brackets is a list.
- **Tuple (constructor: tuple()) -** Tuples are just like `list` except they:
    - Are immutable (cannot be changed once set)
    - Created using parenthesis instead of square brackets
    - There are only 2 tuple methods - [Link](https://www.w3schools.com/python/python_ref_tuple.asp)
- **Dictionary (constructor: dict()) -** A `dict` in Python is the JavaScript object equivalent that stores comma separated key/value pairs. One important difference is that the keys in dictionaries need to be strings. Other than that, everything else is the same.
- **None -**  Python’s version of Ruby’s `nil` or JS’s `null` or `undefined`

## Functions in Python

- Functions in Python are defined using the `def` keyword.
- The name of the function, by convention, is like Ruby - snake_case
- Parameters are still defined in parentheses
- In JS, we used curly braces to define the function body. In Python, we will start the function body with a colon `:` and indent every line in the function body with 4 spaces.
- Use the `return` keyword to return a value from Python functions.
- If you are woking in the Python REPL in your terminal, end a function definition with another space.

## Creating a virtual env

- There are two types of environments that you can set up:
    - Local Python env
    - Virtual Python env
- Your local Python env is going to be the Python related Software and Libraries that you have installed on your machine
- The virtual env is an environment that you can create for a particular project and for this, we will use `pipenv`
- To create a virtual environment using pipenv we can use the following command.
    
    ```bash
    pipenv --python 3.8.13
    ```
    
- The `--python` flag allows us to choose which Python version that we would like to use for this project.
- This command will also generate one file for us:
    - Pipfile - describes the dependencies that we have installed and the Python version.
- We can now install packages like the debugger, `ipdb`
    - `pipenv install ipdb`
- You will notice that we have generated another file - the Pipfile.lock file:
    - Pipfile.lock - describes all the dependencies our dependencies rely on. Like the `npm` package-lock.json file, the Pipfile.lock gives us the ability to reproduce a project env.
    

## Control flow in Python

- `>`: greater than
- `>=`: greater than or equal to
- `<`: less than
- `<=`: less than or equal to
- `==`: equal to
- `!=`: not equal to

## **Logical Operators**

Python has the same logical operators you'll find in many other languages, including JavaScript:

- `and`: **and**. Returns `True` if both statements are true.
- `or`: **or**. Returns `True` if one of the two statements is true.
- `not`: **not**. Coerces the data to its boolean equivalent, then reverses it (`True` becomes `False`, and vice versa).

## List Comprehensions

A list comprehension allows us to instantiate a list object and perform a `for` loop to populate its values in a single line.

## Resources
- List Comprehensions - [W3Schools Link](https://www.w3schools.com/python/python_lists_comprehension.asp)
- Python through a Ruby lens - [Link](https://mikemerin.github.io/Python-through-Ruby/)
- Try/except - [Link](https://www.w3schools.com/python/python_try_except.asp)
- [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Range Docs](https://docs.python.org/3/library/stdtypes.html#ranges)
- [String Methods](https://www.w3schools.com/python/python_ref_string.asp)
- [Generator expressions](https://www.geeksforgeeks.org/generator-expressions/)
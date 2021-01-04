# cs506

This is an example python package for implementing and re-using tools learned in BU CS506

## Setup

You need to have python3 and [pip installed](https://www.makeuseof.com/tag/install-pip-for-python/) on your laptop. If you are using windows, please take a look at [this resource](https://docs.microsoft.com/en-us/windows/python/beginners) for an example set up (terminal, git, IDE etc.).

Additionally, I recommend installing [virtualenv](https://pypi.org/project/virtualenv/1.7.1.2/) (pip install this package) to manage the python packages you install for each project you create.

## Before you Start

Go to your local `CS506-Spring2021/02-library/` folder.

### Optional

Create a virtualenv in this folder (for windows users, please see https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/ for the corresponding commands)

```bash
    virtualenv -p python3 <name-of-your-virtual-env>
```

Activate the virtualenv:

```bash
    source <name-of-your-virtual-env>/bin/activate
```

(to deactivate the environment, just type "deactivate" in your terminal/powershell)

### Required

Install the `cs506` package locally:

```bash
    pip install .
```

Install all the `requirements.txt`

```bash
    pip install -r requirements.txt
```

### Verify your setup

Run the tests with the following command

```bash
    tox 
```

Ensure that all the tests are failing because of a "NotImplementedError" being raised.

## Goal

Take a look at the library functions [here](https://github.com/gallettilance/CS506-Spring2021/blob/master/02-library/cs506/read.py) and [here](https://github.com/gallettilance/CS506-Spring2021/blob/master/02-library/cs506/sim.py).

Remove the

```python
raise NotImplementedError()
```

line and replace it with code that does what the function should do. Test your implementation by running "tox". The goal is to get all tests to pass. Upload your implementations to github by creating a pull request.

## Bonus

It's a good idea to take a look at the tests defined [here](https://github.com/gallettilance/CS506-Spring2021/blob/master/02-library/tests/test_read.py) and [here](https://github.com/gallettilance/CS506-Spring2021/blob/master/02-library/tests/test_sim.py), and add a few tests of your own. Remember to use both positive and negative examples for testing.


Contributions are always welcome (and encouraged) to clarify existing documentation in this repository!

# MyProject

## Install

```
python3 -m venv venv
venv/bin/pip install --upgrade -r requirements.txt
venv/bin/python setup.py develop
```

To avoid having to keep typing `venv/bin` in front of commands, you can
activate your environment (modify certain environment variables like `PATH`)
like this:

```
source venv/bin/activate
```

And to deactivate it:

```
deactivate
```

The rest of the commands in this guide will assume you are running in an
activated Python virtual environment.

## Test

You can run the tests in an activated Python virtual environment like this:

```
nosetests
```

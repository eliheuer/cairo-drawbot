<h1 align="center">
  <a href="https://github.com/eliheuer/CairoDrawBot"><img src="images/icon-4x.gif" alt="DrawBot" width="128" height="128"/></a><br>
  <p>Cairo DrawBot</p>
</h1>

<h4 align="center">A GNU+Linux compatible fork of <a href="https://github.com/typemytype/drawbot">DrawBot</a>.</h4>
<h4 align="center">🚧 This is a work in progress and only aims for basic compatibility with DrawBot. 🚧</h4>
<br>

# Installation guide

First make a Python3 virtual environment to work in, this way all our dependencies are contained in one working directory:
```
python3 -m venv drawbot
```
Now `cd` into the directory and start the virtual environment:
```
cd drawbot
source bin/activate
```
To exit venv at any time enter `deactivate`.

Note: This works for most shells like BASH and ZSH, but if you are using a non-standard shell like fish another method is used.

Now we need to install our dependencies. there is a file in the root directory of this project called requirements.txt, it contains a list of dependencies used to build this project, it should look something like this:
```
cairocffi
numpy
```
Instead of installing each dependency separately, we can install them all at once by entering:
```
pip install -U -r requirements.txt
```
You must have `pip` installed for this to work, see install instructions [here](https://pip.pypa.io/en/stable/installing/).

At any time you can use `pip list` to list the currently installed dependencies.

Now we will install cairodrawbot in editable mode, so we can make changes to the code and test those changes without reinstalling each time. Navigate the root directory of the project and enter:
```
pip install --editable .
```
After installing in editable mode you can run `pip list` and see that our dependencies and cairodrawbot are installed. cairodrawbot should have an extra note showing its location, because it was installed with `--editable`, you should get something like this:
```
(drawbot) > $ pip list
cairocffi (0.8.0)
cairodrawbot (0.0.10, /home/user/drawbot/cairo-drawbot)
cffi (1.11.4)
numpy (1.14.0)
pip (9.0.1)
pycparser (2.18)
setuptools (28.8.0)
```
Now, if everything installed correctly, we can test cairodrawbot by navigating to the `examples/` directory and running one of the example files, like so:
```
cd examples
python example.py
```
A new image should have been generated, look for it in the examples folder.

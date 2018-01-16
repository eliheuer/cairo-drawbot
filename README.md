<h1 align="center">
  <a href="https://github.com/eliheuer/CairoDrawBot"><img src="images/icon-4x.gif" alt="DrawBot" width="128" height="128"/></a><br>
  <p>Cairo DrawBot</p>
</h1>

<h4 align="center">A GNU+Linux compatible fork of <a href="https://github.com/typemytype/drawbot">DrawBot</a>.</h4>

This is a work in progess and only aims for basic compatibility, no GUI is planned at this point. 

## Install

First make a Python3 virtual environment to work in, this way all our dependencies are contained in one working directory:
```
python3 -m venv drawbot
```
Now `cd` into the directory and enter:
```
source bin/activate
```
Note: This works for most shells like BASH and ZSH, but if you are using a non-standard shell like fish another method is used. 

Now we need to install our dependencies. there is a file in the root directory of this project called requirements.txt, it contains a list of dependencies used to build this project, it should look something like this:

```
pycairo==1.15.4
fonttools==3.17.0
ufoLib==2.1.0
defcon==0.3.5
```
Instead of installing each dependency sepratly, we can install them all at once by entering: 
```
pip install -U -r requirements.txt 
```
You must have `pip` installed for this to work, see install instructions [here](https://pip.pypa.io/en/stable/installing/).

[![Build Status](https://travis-ci.com/gaetangr/P8_pur_beurre.svg?branch=development)](https://travis-ci.com/gaetangr/P8_pur_beurre)
![PurBeurre Build](https://github.com/gaetangr/P8_pur_beurre/workflows/PurBeurre%20Build/badge.svg?event=push)
# ✨ Pur Beurre ✨

Pur beurre is an application that help you eat better

## Summary 📋

- [Getting started](#getting-started)
- [Installing](#installing)
- [Prerequisites](#prerequisites)
- [Built with](#built-with)
- [Authors](#authors)

## Getting Started 🚀

These instructions will guide to test the project on your own or you local machine

### Prerequisites

If you wish to test the code online : [to be completed]

Make sure to have Python 3x installed on your computer
Run the following in your command prompt

```
python
```

I used **Python 3.8.0** to built this program, Python 3.0 to 3.8 will work.

### Installing

N.B : As a convenience I have created a custom command to create a superuser in no time, run the following command:

```
python manage.py super_account
```


A step by step that tell you how to get my code up and running on your local machine :

- Clone my repo

```
git clone https://github.com/Mcflan-7/P8_pur_beurre.git
```

- Set up your virtual environnement (using venv for this example, any will do)

```
python -m venv venv
```

- Activate your virtual environement with

  ```
  Windows: source venv/Scripts/activate
  MacOS: source venv/bin/activate
  ```

- Install the requirement with

```
pip install -r requirements.txt
```

- CD to the app directory

```
cd prometheus
```

- Export the app and run flask

```
export FLASK_APP=index.py
python -m flask run

```

## Built With 🛠

- [Python](<[https://www.python.org/](https://www.python.org/)>) - The programming language that lets you work quicklyand integrate systems more effectively
- [Flask](<[https://flask.palletsprojects.com/en/1.1.x/(https://flask.palletsprojects.com/en/1.1.x/)>) - Web development one drop at a time
- [VSCODE](<[https://code.visualstudio.com/](https://code.visualstudio.com/)>) - The code editing redefined

## Authors 💻

- **Gaëtan GROND** - _Initial work_ - [GITHUB](<[https://github.com/Mcflan-7](https://github.com/Mcflan-7)>)


coverage report --omit="*/virtualenvs/*,admin.py,config/*,*/migrations/*,manage.py"
```
coverage report --omit='venv*','config/*','/migrations/'
```
```

```

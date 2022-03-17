# New OPF
This is a new version to Optimum Property Fix.

## Virtual Environment
To run this project, your system will need to install a handful of packages. Please create a python3 virtual environment, so the packages would all be located in one place. 

### Make a Virtual Environment
Please run the following command to create a virtual environment.

``` bash
python3 -m venv env
```
### Go Into Virtual Environment
To use the virtual environment to run the project, please do the following command.

```bash
. env/bin/activate
```

### Install Packages
Please install the following using package manager pip in the virtual enviornment.

```bash
pip install flask
pip install flask-SQLAlchemy
pip install SQLAlchemy
pip install jinja2
pip install flask-login
pip install flask-principal
```

### Run the Project
To run the project for the first time, please do the following commands.

```bash
export FLASK_APP=view
export FLASK_ENV=development
```
If you have done the two commands, to run or rerun the project, do the following command.

``` bash
flask run
```

## Collaborators

### Team Members:
    Aisha Co
    Melissa Flores
    Nasrin Juana

### Advisor
    Erin Keith


IF EXIST ..\venv\venv_fin\NUL GOTO NO_CREATE

cd ..\
md venv
cd venv

call python -m venv  venv_fin

cd ..\Financiar



:NO_CREATE


call ..\venv\venv_fin\Scripts\activate.bat  

set https_proxy=http://192.168.1.29:8080


if [%1] == [r] call pip install -r django_cms\requirements.txt

if [%1] == [s] or [%2] == [s] call python django_cms\manage.py runserver 0:5500

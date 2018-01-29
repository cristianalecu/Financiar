
IF EXIST ..\venv\venv_fin\NUL GOTO NO_CREATE

cd ..\
md venv
cd venv

call python -m venv  venv_fin

cd ..\Financiar


:NO_CREATE

call ..\venv\venv_fin\Scripts\activate.bat  


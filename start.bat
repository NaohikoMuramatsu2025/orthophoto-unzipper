@echo off
REM ���z��������΂����ŗL�����i��j
::call conda activate gis_env

REM �X�N���v�g�̂���f�B���N�g���ֈړ�
cd /d "%~dp0\Python_SRC"

REM Python�X�N���v�g�̎��s
::python "extract_ndvi - �R�s�[ (5).py"
python unzip_orthos.py

pause

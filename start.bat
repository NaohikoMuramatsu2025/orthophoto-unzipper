@echo off
REM 仮想環境があればここで有効化（例）
::call conda activate gis_env

REM スクリプトのあるディレクトリへ移動
cd /d "%~dp0\Python_SRC"

REM Pythonスクリプトの実行
::python "extract_ndvi - コピー (5).py"
python unzip_orthos.py

pause

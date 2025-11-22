@echo off
echo Installing yandex-music...
pip install yandex-music

echo Running script...
python forYandex.py

echo Cleaning up...
pip uninstall yandex-music -y

echo Done!
pause
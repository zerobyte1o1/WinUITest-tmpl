@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=c:/result
allure generate c:/result -o c:/allure-report
@REM allure serve ./result/ -p 8765


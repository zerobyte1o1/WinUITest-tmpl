@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp

start /B /WAIT allure generate --clean ./result/temp -o ./result/allure-report
call timeout /t 5 > nul&report.bat



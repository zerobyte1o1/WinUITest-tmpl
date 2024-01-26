set /p version=<c:/dish.listen

start /B allure-combine --auto-create-folders c:/winuitest-AIDish/result/allure-report --dest c:/allure-html/%version%

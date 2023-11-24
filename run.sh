pytest testCase/ --alluredir=./result --clean-alluredir

/opt/homebrew/bin/allure generate ./result -c -o ./result/report/

/opt/homebrew/bin/allure serve ./result/ -p 8765
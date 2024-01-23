import subprocess


def run_test():
    run_pytest()
    run_allure_serve()


def run_pytest():
    # Replace with your pytest command
    pytest_cmd = "pytest testCase/ --alluredir=./result"
    # Execute the pytest command
    subprocess.run(pytest_cmd, shell=True)


def run_allure_serve():
    # Replace with your allure serve command
    allure_cmd = "allure serve ./result/ -p 8765"
    # Execute the allure serve command
    subprocess.run(allure_cmd, shell=True)


run_test()

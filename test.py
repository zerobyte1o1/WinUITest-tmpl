import inspect

import inspect

class MyClass:
    def my_method(self):
        caller = inspect.currentframe().f_back.f_code.co_name
        print("Method", caller, "called this method.")

class AnotherClass:
    def another_method(self):
        obj = MyClass()
        obj.my_method()

another = AnotherClass()
another.another_method()
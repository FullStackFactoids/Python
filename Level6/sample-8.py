import inspect

def example_function(param1, param2):
    pass

sig = inspect.signature(example_function)
print(sig.parameters)  # Output: OrderedDict([('param1', <Parameter "param1">), ('param2', <Parameter "param2">)])

# Fun Facts

import inspect

class ExampleClass:
    def method_in_class(self):
        pass

print(inspect.isclass(ExampleClass))  # Output: True
print(inspect.ismethod(ExampleClass.method_in_class))  # Output: True
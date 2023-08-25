import json

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

json_str = json.dumps(data)
print(json_str)  # Output: '{"name": "John", "age": 30, "city": "New York"}'

# Fun Facts
import json

json_str = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_str)
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

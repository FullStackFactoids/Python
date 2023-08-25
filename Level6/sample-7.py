from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = open("file.txt", "w")
    try:
        yield resource
    finally:
        resource.close()

with managed_resource() as r:
    r.write("Hello, World!")
# The file is automatically closed after the block.

#Fun Facts

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)
# The page is automatically closed after the block.

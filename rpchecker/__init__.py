__version__ = "1.0.0"
"""Check site connectivity with your own functions.
>>> python -m rpchecker -h
usage: rpchecker [-h] [-u URLs [URLs ...]] [-f FILE] [-a]

check the availability of web sites

options:
  -h, --help            show this help message and exit
  -u URLs [URLs ...], --urls URLs [URLs ...]
                        enter one or more website URLs
  -f FILE, --input-file FILE
                        read URLs from a file
  -a, --asynchronous    run the connectivity check asynchronously


# Synchronous execution
>>> cat sample-urls.txt
python.org
pypi.org
docs.python.org
peps.python.org

>>> python -m rpchecker -f sample-urls.txt\n
The status of "python.org" is: "Online!" 👍
\nThe status of "pypi.org" is: "Online!" 👍
\nThe status of "docs.python.org" is: "Online!" 👍
\nThe status of "peps.python.org" is: "Online!" 👍

>>> python -m rpchecker -u python.org pypi.org docs.python.org
The status of "python.org" is: "Online!" 👍
The status of "pypi.org" is: "Online!" 👍
The status of "docs.python.org" is: "Online!" 👍


# Asynchronous execution
>>> python -m rpchecker -u python.org pypi.org docs.python.org -a
The status of "pypi.org" is: "Online!" 👍
The status of "docs.python.org" is: "Online!" 👍
The status of "python.org" is: "Online!" 👍

"""
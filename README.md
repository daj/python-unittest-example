A minimal example of a Python project which utilizes both `unittest` and `logging`.

## Running the script

```
$ python utils.py
Hello
```

The logs are written to `utils.log`.

```
$ cat utils.log 
INFO:root:Initialized
DEBUG:root:Example log
```

## Running automated tests

If you don't already have the `unittest` dependency, install it:

```
pip install unittest
```

To run all the tests, run:

```
python -m unittest discover -v
```
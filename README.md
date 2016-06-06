# Rollup filter for webassets [![Build Status](https://travis-ci.org/rclmenezes/webassets-rollup.svg?branch=master)](https://travis-ci.org/rclmenezes/webassets-rollup)


Filter for compiling assets using [Rollup](http://rollupjs.org) and [webassets](http://webassets.readthedocs.org). Requires Python 2.7 or Python 3.3 and newer.

## Basic usage

```python
from webassets.filter import register_filter
from webassets_rollup import Rollup

register_filter(Rollup)
```

## Options

##### ROLLUP_BIN

The path to the Rollup binary. If not set, assumes `rollup` is in the system path.

##### ROLLUP_EXTRA_ARGS

A list of any command-line arguments to be included when `rollup` is called. For example:

```python
ROLLUP_EXTRA_ARGS = ['--no-strict', '-f', 'cjs']
```

## License

MIT

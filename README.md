# Mkdocs-Matplotlib

[![PyPI version](https://badge.fury.io/py/mkdocs-matplotlib.svg)](https://badge.fury.io/py/mkdocs-matplotlib)
[![Test](https://github.com/AnHo4ng/mkdocs-matplotlib/actions/workflows/test.yml/badge.svg)](https://github.com/AnHo4ng/mkdocs-matplotlib/actions/workflows/test.yml)
[![Release Pipeline](https://github.com/AnHo4ng/mkdocs-matplotlib/actions/workflows/release.yml/badge.svg)](https://github.com/AnHo4ng/mkdocs-matplotlib/actions/workflows/release.yml)
[![Code Quality](https://github.com/AnHo4ng/mkdocs-matplotlib/actions/workflows/conde_quality.yml/badge.svg)](https://github.com/AnHo4ng/mkdocs-matplotlib/actions/workflows/conde_quality.yml)
[![Documentation Status](https://readthedocs.org/projects/mkdocs-matplotlib/badge/?version=latest)](https://mkdocs-matplotlib.readthedocs.io/en/latest/?badge=latest)
[![Python version](https://img.shields.io/badge/python-3.8-blue.svg)](https://pypi.org/project/kedro/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/AnHo4ng/mkdocs-matplotlib/blob/master/LICENCE)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)

**Mkdocs-Matplotlib** is a plugin for [mkdocs](https://www.mkdocs.org/) which allows you to automatically generate matplotlib figures and add them to your documentation.
Simply write the code as markdown into your documention.

![screenshot](docs/assets/screenshot.png)

## Quick Start

This plugin can be installed with `pip`

```shell
pip install mkdocs-matplotlib
```
To enable this plugin for mkdocs you need to add the following lines to your `mkdocs.yml`.

```yaml
plugins:
  - mkdocs_matplotlib
```

To render a code cell using matplotlib you simply have to add the comment `# mkdocs: render` at the top of the cell.

```python
# mkdocs: render
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
```

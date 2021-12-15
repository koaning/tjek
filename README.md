<img src="icon.svg" width=125 height=125 align="right">

# tjek

> tjek changes with the main branch

| Command | Description |
| --- | --- |
| `version` | Shows the version of `tjek` |
| `diffs` | Show files that differ from the main branch |
| `ifchanged` | Runs a command if specific files changed |

## Install

```
python -m pip install tjek
```

## Quickstart 

This app is useful when you want to limit certain CI steps based
on which files have changed. For example; you might

## CLI Documentation

Tjek helps you understand changed git files.

**Usage**:

```console
$ tjek [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `diffs`: List updated files compared to another...
* `ifchanged`: List updated files compared to another...
* `version`: Gives the version of the app

## `tjek diffs`

List updated files compared to another branch.

**Usage**:

```console
$ tjek diffs [OPTIONS]
```

**Options**:

* `--branch TEXT`: Branch to compare against.  [default: origin/main]
* `--help`: Show this message and exit.

## `tjek ifchanged`

List updated files compared to another branch.

**Usage**:

```console
$ tjek ifchanged [OPTIONS] FILES... COMMAND
```

**Arguments**:

* `FILES...`: The file to count the words in.  [required]
* `COMMAND`: Command to run if need changes are detected.  [required]

**Options**:

* `--branch TEXT`: Branch to compare against.  [default: origin/main]
* `--verbose / --no-verbose`: Show extra info.  [default: False]
* `--help`: Show this message and exit.

## `tjek version`

Gives the version of the app

**Usage**:

```console
$ tjek version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## Python Documentation 

The python library exposes a single function that can be used
to help detect files that have changed. 

```python
from tjek import find_changed_files

find_changed_files()
```

This is *super* useful when you're building a static website
([exibit A](https://calmcode.io)) and you're only interested 
in building the few markdown files that have changed. This might
cause a serious speedup!

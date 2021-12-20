<img src="icon.png" width=125 height=125 align="right">

# tjek

> tjek changes with the main branch

<br>

This project gives you a minimal method to check which files
changed in a git project such that you only need to run your
checks against these files. There's a few use-cases for it: 

- This can help prevent pytest from running every single unit 
test even if only a few changes have been made.
- Static site builders could use it to only build the
markdown files that are different than the main branch. This 
may seriously reduce the build time locally.

## Install

```
pip install https://github.com/user/repo.git@branch
```

## Quickstart 

This app is useful when you want to limit certain CI steps based
on which files have changed. For example; you might

## CLI Documentation

Tjek helps you understand changed git files.

```
> tjek --help

Tjek helps you understand changed git files.

Options:
  --help  Show this message and exit.

Commands:
  diffs      List updated files compared to another branch.
  ifchanged  Run a CLI command if specific files changed.
  version    Gives the version of the app
```

<details>
  <summary><code>tjek diffs</code></summary>
  </br>

List updated files compared to another branch.

**Usage**:

```console
$ tjek diffs [OPTIONS]
```

**Options**:

* `--branch TEXT`: Branch to compare against.  [default: origin/main]
* `--help`: Show this message and exit.

</details>

<details>
  <summary><code>tjek ifchanged</code></summary>
  </br>

Run a CLI command if specific files changed.

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

</details>


<details>
  <summary><code>tjek version</code></summary>
  </br>

Gives the version of the app

**Usage**:

```console
$ tjek version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

</details>

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

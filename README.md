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

## Docs 

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
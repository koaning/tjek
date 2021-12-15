from typing import List
from pathlib import Path
import subprocess

import typer

from tjek import find_changed_files


app = typer.Typer(name="tjek", add_completion=False, help="Tjek helps you understand changed git files.")


@app.command()
def version():
    """Gives the version of the app"""
    typer.echo(f"0.1.0")

@app.command()
def diffs(branch: str = typer.Option("origin/main", help="Branch to compare against.")):
    """List updated files compared to another branch."""
    typer.echo("\n".join(find_changed_files(branch=branch)))


@app.command()
def ifchanged(files: List[Path] = typer.Argument(..., help="The file to count the words in."),
              command: str = typer.Argument(..., help="Command to run if need changes are detected."),
              branch: str = typer.Option("origin/main", help="Branch to compare against."),
              verbose: bool = typer.Option(False, is_flag=True, help="Show extra info.")):
    """Run a CLI command if specific files changed."""
    changed_files = [Path(_) for _ in find_changed_files(branch=branch)]

    for path in files:
        if not path.exists():
            typer.echo(f"Path {path} doesn't seem to exist.")
            raise typer.Exit(code=1)

    if verbose:
        for f in files:
            if f in changed_files:
               typer.echo(f"Change detected in {f}")
        if not any([f in changed_files for f in files]):
            typer.echo(f"No changes detected.")

    if any([f in changed_files for f in files]):
        subprocess.run(command, shell=True)


if __name__ == "__main__":
    app()

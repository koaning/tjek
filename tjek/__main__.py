import typer
import subprocess

app = typer.Typer(name="tjek", add_completion=False, help="Tjek helps you understand changed git files.")

@app.command()
def version(name):
    """Gives the version of the app"""
    typer.echo(f"0.0.1")

@app.command()
def diffs(branch: str = typer.Argument("main", help="Branch to compare against.")):
    """List updated files compared to another branch."""
    print(" ".join(["git", "diff", "--name-status", branch]))
    subprocess.run(["git", "diff", "--name-status", branch, "|", "cat"])

if __name__ == "__main__":
    app()

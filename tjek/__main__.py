import typer
import subprocess

app = typer.Typer(name="tjek", add_completion=False, help="Tjek helps you understand changed git files.")

@app.command()
def version():
    """Gives the version of the app"""
    typer.echo(f"0.0.1")

@app.command()
def diffs(branch: str = typer.Option("origin/main", help="Branch to compare against.")):
    """List updated files compared to another branch."""
    typer.echo("\n".join(find_changed_files(branch=branch)))
    
def find_changed_files(branch):
    """Use subprocess to find all files that are different."""
    output = subprocess.run(["git", "--no-pager", "diff", "--name-status", branch], capture_output=True)
    files = [s[s.find("\\t")+2:] for s in str(output.stdout).split("\\n")]
    return [s for s in files if len(s) > 0]

if __name__ == "__main__":
    app()

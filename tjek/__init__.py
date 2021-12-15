import subprocess

def find_changed_files(branch):
    """Use subprocess to find all files that are different."""
    output = subprocess.run(["git", "--no-pager", "diff", "--name-status", branch], capture_output=True)
    files = [s[s.find("\\t")+2:] for s in str(output.stdout).split("\\n")]
    return [s for s in files if len(s) > 0]

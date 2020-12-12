import subprocess

default_command = ['', '']

specify_commit = input("Specify commit? y/n ")
if specify_commit == "y":
    commit = input("Commit SHA: ")
else:
    specify_branch = input("Specify branch? y/n ")
    if specify_branch == "y":
        commit = input("Branch name: ")
    else:
        commit = "master"



list_files = subprocess.run(["echo", commit])
print("The exit code was: %d" % list_files.returncode)

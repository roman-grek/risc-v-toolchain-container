import subprocess

command_args = ""
commit = "master"
arch = "rv64imac"

specify_commit = input("Specify commit? y/n ")
if specify_commit == "y":
    commit = input("Commit SHA: ")
else:
    specify_branch = input("Specify branch? y/n ")
    if specify_branch == "y":
        commit = input("Branch name: ")

specify_arch = input(f"Specify architecture ({arch} by default)? y/n ")
if specify_arch == "y":
    arch = input("Arch: ")

add_args = input (f"Current command is `./configure--with-arch=${arch}`. Want to add args? y/n ")
if add_args == "y":
    command_args = input("Additional args: ")

with open(".env", "w") as env_file:
    env_file.writelines([f'RISCV_COMMIT="{commit}"\n', f'RISCV_ARGS="{command_args}"\n',  f'RISCV_ARCH="{arch}"'])

subprocess.run(["docker-compose", "up"])
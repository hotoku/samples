import subprocess as sp


with sp.Popen(["sudo", "cat", "6.py"], stdout=sp.PIPE) as p1:
    with sp.Popen(["grep", "with"], stdin=p1.stdout, stdout=sp.PIPE) as p2:
        print(p2.stdout.read().decode("utf-8"))
print(p1.returncode)
print(p2.returncode)

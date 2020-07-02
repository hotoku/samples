import subprocess


with open("8.out", "w") as f:
    po = subprocess.Popen(["python", "-c", "while True: print(1)"], stdout=f, stderr=subprocess.STDOUT, text=True)
print(po.pid)

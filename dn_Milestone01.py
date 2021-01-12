import os

thisdir = os.getcwd()

for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".pdf"):
            print(os.path.join(r, file))
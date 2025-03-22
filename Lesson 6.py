import os

path = "C:\\Users\\gololobov\\Downloads"
# path = "C:/Users/gololobov/Downloads/"
path = os.path.normpath(path)
# print(path)

# for path, dirname, filenames in os.walk(path):
#     print(path)
#     print(dirname)
#     print(filenames)

# dir = "Test"

# path = os.path.join(path, dir)
# os.mkdir(path)


# path = "C:\\Users\\gololobov\\Downloads\\Test\\text.txt"
#
# print(os.path.isdir(path))
# print(os.path.isabs(path))
# print(os.path.isfile(path))
# print(os.path.islink(path))
#
# print(os.path.getctime(path))
# print(os.path.getmtime(path))
# print(os.path.getatime(path))
# print(os.path.getsize(path))


# f = open("../../Downloads/Test/text.txt", "w")
# f.write("Hello Python")
# f.close()

# f = open("text.txt", "r")
# st = f.read()
# f.close()
# print(st)

path = "C:\\Users\\gololobov\\Downloads\\Logo"

def spy(path):
    path = os.path.normpath(path)
    result = {"dirs":[], "files":[]}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    with open("spy.txt", "w") as f:
        f.write("DIRECTIRIES\n")
        for dir in result["dirs"]:
            f.write(f"[{dir.upper()}]\n")
        f.write("\n")
        f.write("FILES\n")
        for file in result["files"]:
            f.write(f"{file}\n")

spy(path)
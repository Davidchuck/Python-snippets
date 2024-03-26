from pathlib import Path
# path=Path("test")
# print(path.mkdir()) #creates the test directory if it doesnt exist
# print(path.rmdir()) #removes/deletes the directory
path=Path()
for file in path.glob('*.py'):
    print(file)
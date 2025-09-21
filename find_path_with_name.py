import os

def find_file(filename, search_path="C:/"):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

if __name__=='__main__':
    print(find_file("data.csv", "C:/"))   # Windows
# print(find_file("example.txt", "/"))   # Linux/macOS

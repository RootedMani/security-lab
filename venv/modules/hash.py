import hashlib 

def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path, "rb") as file: 
        while True:
            chunk = file.read(1024)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    print(f"The hash equivelant of the given text file is: {hash_file("venv/sample_files/sample.txt")}")

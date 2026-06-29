import hashlib 

def hash_file(file_path):
    """ Take a relative file path and return its hash equivalent.

        Args:
            file_path (str): A string which represents a relative file path to a text file.

        Returns:
            SHA-256 hash equivalent of the given text in hexodecimal, human-readable format.
    """
    h = hashlib.new("sha256") # Create a SHA-256 hash object

    with open(file_path, "rb") as file: # Open file in binary mode
        while True: # Loop unitl the end of the file
            chunk = file.read(1024) # Read 1024 bytes at a time
            if not chunk: # When reach empty (end of the file)
                break # break the loop
            h.update(chunk) # Add the chunk to hash calculation
    return h.hexdigest() # return hash in hexodecimal format

def verify_integrity(file1: str , file2: str):
    """ Checks if two files are identical by checking their hash equivalent 
    Args:
        file1 (str): Relative path to the first file
        file2 (str): Relative path to the second file 
    Returns: 
        str: A message indicating whether the two files given are identical
        or have been modified.
    Note:
        Print a message before returning the result.
    """
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    print(f"Checking integrity between {file1} and {file2}")
    if hash1 == hash2:
        return "The 2 files are intact. No modification has been made."
    # Else
    return "The two files are modified. Possibly unsafe."

if __name__ == "__main__":
    print(f"The hash equivelant of the given text file is: {hash_file('venv/sample_files/sample.txt')}\n")
    print(verify_integrity(r"venv/sample_files/sample_image1.jpeg", r"venv/sample_files/sample_image2.jpeg"), "\n")
    print(verify_integrity(r"venv/sample_files/sample_image1.jpeg", r"venv/sample_files/sample_image3.jpeg"))
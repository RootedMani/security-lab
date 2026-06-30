# Security Lab

A command-line toolkit for experimenting with core cryptography and security concepts in Python: symmetric and asymmetric encryption, file hashing, integrity verification, and password strength/hashing.

## Features

- **Encryption** — Encrypt and decrypt text using either AES-GCM (symmetric) or RSA-OAEP (asymmetric).
- **Hashing** — Generate a SHA-256 hash of a file or an arbitrary message.
- **File integrity verification** — Compare two files by hash to detect whether they've been modified.
- **Password strength check** — Evaluate password strength using `zxcvbn`, with feedback and suggestions for weak passwords.
- **Password hashing & verification** — Hash passwords with `bcrypt` and verify a re-entered password against the stored hash.

## Project structure

```
security_lab/
├── main.py              # CLI entry point and menu
├── modules/
│   ├── encryption.py    # AES-GCM and RSA encryption/decryption
│   ├── hash_file.py     # SHA-256 file hashing and integrity verification
│   └── password.py      # Password strength checking, hashing, and verification
├── sample_files/         # Sample files for testing hashing/integrity checks
├── requirements.txt
└── venv/                 # Python virtual environment (not committed to version control)
```

## Requirements

- Python 3.12+
- A virtual environment is recommended (the project assumes one named `venv/`)

### Dependencies

- [`cryptography`](https://pypi.org/project/cryptography/) — AES-GCM and RSA encryption
- [`zxcvbn`](https://pypi.org/project/zxcvbn/) — password strength estimation
- [`bcrypt`](https://pypi.org/project/bcrypt/) — password hashing

## Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd security_lab

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the program from the project root:

```bash
python main.py
```

You'll be presented with a menu:

```
Choose an operation (from 1 to 4)
1. Encryption
2. Hashing
3. Integrity verification (for files)
4. Checking a password's strength
```

### 1. Encryption

Choose between AES-GCM or RSA, then enter a message to encrypt. The program prints both the encrypted (hex-encoded) and decrypted text so you can confirm the round trip works.

### 2. Hashing

Choose to hash either a file (by relative path) or a typed message. File hashing reads the file in chunks and returns a SHA-256 digest in hex.

### 3. Integrity verification

Provide two relative file paths. The program hashes both and reports whether they're identical or have been modified — useful for confirming a file hasn't been tampered with or corrupted.

### 4. Password strength check

Enter a password (input is hidden via `getpass`). The program rejects weak passwords and re-prompts until a strong one is given, then hashes it with `bcrypt` and verifies a re-entered confirmation password against the hash.

## Sample files

The `sample_files/` directory contains a text file and a few JPEGs you can use to test hashing and integrity verification without needing your own files. As you can see the first and the second files are identical and third one is different. It's a good example to see how integrity verification in this project works.

## Notes

- This is a learning/lab project for exploring cryptographic primitives — it has not been audited and should not be used as-is to protect real secrets in production.
- RSA encryption here generates a fresh keypair on every call, so it's best understood as a demonstration of the encrypt/decrypt flow rather than a persistent key-management setup.
- `venv/` should be excluded from version control

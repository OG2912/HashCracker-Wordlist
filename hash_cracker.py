#!/usr/bin/env python3

import hashlib
import argparse
import sys
import os

supported_hashes = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512
}

def crack_hash(target_hash, hash_type, wordlist_path):
    if hash_type not in supported_hashes:
        print("[-] Unsupported hash type.")
        return

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for word in f:
                word = word.strip()
                hash_func = supported_hashes[hash_type]()
                hash_func.update(word.encode('utf-8'))
                if hash_func.hexdigest() == target_hash:
                    print(f"[+] Hash cracked! Plaintext: {word}")
                    return
        print("[-] No match found in wordlist.")
    except FileNotFoundError:
        print("[-] Wordlist file not found.")

def main():
    parser = argparse.ArgumentParser(description="Hash Cracker (Wordlist-based)")
    parser.add_argument("-t", "--type", required=True, help="Hash type: md5, sha1, sha256, sha512")
    parser.add_argument("-H", "--hash", required=True, help="Target hash to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")

    args = parser.parse_args()
    crack_hash(args.hash, args.type.lower(), args.wordlist)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[*] Tip: You don't need root for this tool.")
    main()

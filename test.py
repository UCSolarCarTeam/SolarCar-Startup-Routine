import sys, subprocess

def main():
    p = subprocess.Popen([sys.argv[1]])
    p2 = subprocess.Popen([sys.argv[2], sys.argv[3]])

    while True:
        if (p.poll() is not None):
            print sys.argv[1] + " died"
            p = subprocess.Popen([sys.argv[1]])
            p2 = subprocess.Popen([sys.argv[2], sys.argv[3]])

if __name__ == '__main__':
    main()
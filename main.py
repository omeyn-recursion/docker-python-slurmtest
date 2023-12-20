import sys
import socket
import datetime

def main():
    print("Slurm test starting")
    print(f"args {sys.argv}")
    now = datetime.datetime.now().timestamp()
    host = socket.gethostname()
    path = sys.argv[1]
    filename = path + host + '_' + str(now) + '.txt'
    f = open(filename, "a")
    f.write("Now the file has more content!")
    f.close()

if __name__ == "__main__":
    main()
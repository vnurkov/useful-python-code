from second import df_func
import subprocess


def tmp_disk():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print("Space used in /tmp directory")
    subprocess.call([tmp_usage, tmp_arg, path])


def main():
    df_func()
    tmp_disk()


if __name__ == "__main__":
    main()

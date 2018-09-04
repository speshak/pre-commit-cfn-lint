import argparse
import subprocess


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        if subprocess.call(['cfn-lint', filename]) != 0:
            retcode = 1

    return retcode


if __name__ == '__main__':
    exit(main())

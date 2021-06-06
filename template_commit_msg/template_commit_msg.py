#!/usr/bin/python
import sys
import argparse
from pathlib import Path
import git



def main(argv=None):
    exit_code = False
    missing_from_git = []

    parser = argparse.ArgumentParser()
    parser.add_argument('--pattern', type=str, required=True)
    parser.add_argument('filenames', type=str, help='It will ignore file names.')
    args = parser.parse_args()
    repository = git.Repo('.', search_parent_directories=True)
    untracked = set(repository.untracked_files)
    modified = []

    original = Path(args.filenames).read_text()
    Path(args.filenames).write_text(args.pattern+'\n'+original)

    if exit_code:
        sys.exit(1)


if __name__ == '__main__':
    main()

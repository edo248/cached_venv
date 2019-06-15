# -*- coding: utf-8 -*-

"""Console script for cached_venv."""
import sys
import click
import hashlib
import os
import tarfile
import virtualenv
from pip._internal import main as pipmain


cache_dir = os.path.expanduser("~/.cache/cached-venvs")
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)


@click.command()
@click.argument("requirements", type=click.Path(exists=True))
@click.argument("venvname", required=False, default="./.venv")
def main(requirements, venvname):
    print(f"Creating venv from {requirements} in {venvname}")

    # hash requirements
    content = open(requirements, "r").read().encode()
    checksum = hashlib.sha256(content).hexdigest()
    print(f"Requirements file has checksum: {checksum}")
    # check cache for hash
    cache_path = os.path.join(cache_dir, f"{checksum}.tar.gz")
    if os.path.exists(cache_path):
        #  unzip from cache
        archive = tarfile.open(cache_path)
        archive.extractall(path=venvname)
        archive.close()
    else:
        #  create venv from scratch
        # create and activate the virtual environment
        print(f"Not found in cache, creating")
        virtualenv.create_environment(venvname)
        # pip install a package using the venv as a prefix
        pipmain(["install", "-r", requirements, "--prefix", venvname])

        #  cache venv
        tar = tarfile.open(cache_path, "w:gz")
        for path, a, b in os.walk(venvname):
            relpath = os.path.relpath(path, venvname)
            tar.add(path, relpath)
        tar.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

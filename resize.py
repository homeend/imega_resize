import multiprocessing
import os
import sys
from contextlib import contextmanager
from functools import partial
from subprocess import call
from pathlib import Path


@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()


def resize_image(resize_percent: str, file_path: Path):
    exec_cmd = (
        "t:\\ImageMagick\\convert.exe -resize "
        + resize_percent
        + "% "
        + str(file_path)
        + " "
        + str(file_path)
    )
    print(exec_cmd)
    os.system(exec_cmd)


if __name__ == "__main__":
    resize_percent = "50"

    if len(sys.argv) == 2:
        resize_percent = sys.argv[1]

    with poolcontext() as pool:
        pool.map(partial(resize_image, resize_percent), (file_path for file_path in Path.cwd().glob("*") if file_path.suffix in {".jpg", ".png"}))

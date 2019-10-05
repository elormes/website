import os
import errno
import shutil

import markdown


def mkdir_if_not_exists(dir_):
    if not os.path.isdir(dir_):
        os.mkdir(dir_)

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print("Directory not copied: Error {}".format(e))


if __name__ == "__main__":

    # check if in root folder
    assert os.path.basename(os.getcwd()) == "website"
    mkdir_if_not_exists("build")

    build_dirs = ["build/html"]

    src_dest_tuples = [["src/css", "build/css"],
                ["src/fonts", "build/fonts"],
                ["src/images", "build/images"]]
    
    with open("src/html/base.html", "r") as f:
        base = "".join(line for line in f.readlines())

    with open("src/md/about.md", "r") as f:
        md = "".join(line for line in f.readlines())
        content = markdown.markdown(md)

    for t in src_dest_tuples:
        copy(t[0], t[1])

    mkdir_if_not_exists("build/html")
    with open("build/html/about.html", "w") as f:
        f.writelines(base.format(body=content))

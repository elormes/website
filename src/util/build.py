import os
import errno
import shutil

import markdown


BASE_HTML = "src/html/base.html"

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

def make_html_pages_from_md(dir_):
    html_dest = "build/html"
    with open(BASE_HTML, "r") as f:
        base = "".join(line for line in f.readlines())

    files = [f for f in os.listdir(dir_)
             if os.path.isfile(os.path.join(dir_, f))
             and f.endswith(".md")]

    for f in files:
        with open(os.path.join(dir_, f), "r") as md:
            text = "".join(line for line in md.readlines())
            content = markdown.markdown(text, extensions=["attr_list"])

        mkdir_if_not_exists(html_dest)
        page_name = f.split(".")[0] + ".html"
        with open(os.path.join(html_dest, page_name), "w") as webpage:
            webpage.writelines(base.format(body=content))



if __name__ == "__main__":

    # check if in root folder
    assert os.path.basename(os.getcwd()) == "website"
    mkdir_if_not_exists("build")

    build_dirs = ["build/html"]

    src_dest_tuples = [["src/css", "build/css"],
                ["src/fonts", "build/fonts"],
                ["src/images", "build/images"]]

    # copy resources to build
    for t in src_dest_tuples:
        copy(t[0], t[1])

    md_dir = "src/md/"
    assert os.path.isdir(md_dir)
    
    make_html_pages_from_md(md_dir)


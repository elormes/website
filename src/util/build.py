import os
import errno
import shutil

import markdown


ROOT = "website"
SRC_DIR = "src"
BUILD_DIR = "build"
MD_DIR = f"{SRC_DIR}/md"

# list of folders in SRC_DIR to be copied to BUILD_DIR
ASSET_DIRS = ["css", "fonts", "images", "posts"]

# preload base html
with open("src/html/base.html", "r") as f:
    base_html = "".join(line for line in f.readlines())

def mkdir_if_not_exists(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print("Directory not copied: Error {}".format(e))

def get_md_files(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            filepath = os.path.abspath(os.path.join(dirpath, f))
            if filepath.endswith(".md"):
                yield filepath

def page_source_from_md(markdown_file):
    with open(markdown_file, "r") as md:
        page_title = md.readline() # first line of markdown file reserved for page title
        text = "".join(line for line in md.readlines())
        content = markdown.markdown(text, extensions=["attr_list"])
    
    return base_html[:].format(title=page_title, body=content)


if __name__ == "__main__":

    # check if script was launched from root folder
    assert os.path.basename(os.getcwd()) == ROOT

    mkdir_if_not_exists(BUILD_DIR)

    # copy assets to build
    for dirname in ASSET_DIRS:
        copy(f"{SRC_DIR}/{dirname}", f"{BUILD_DIR}/{dirname}")

    assert os.path.isdir(MD_DIR)

    # convert markdown to html and write to html files in BUILD_DIR
    for filepath in get_md_files(MD_DIR):
        basedir, filename = os.path.split(filepath)
        webpage_name = filename.split(".")[0] + ".html"
        dest = f"{BUILD_DIR}/{basedir.split(MD_DIR)[-1]}"
        mkdir_if_not_exists(dest);

        with open(os.path.join(dest, webpage_name), "w") as webpage:
            webpage.writelines(page_source_from_md(filepath))

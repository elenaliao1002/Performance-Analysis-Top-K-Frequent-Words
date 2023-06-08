import os
import subprocess as sp


def fetch_file(data, out_dir):
    if not os.path.isdir(out_dir):
        download = ["wget", "-qO", f"{out_dir}", f"{data}"]
        steps = [download]
        if out_dir.endswith(".zip"):
            unzip = ["unzip", f"{out_dir}"]
            if os.path.isdir("__MACOSX"):
                remove = ["rm", "-r", "__MACOSX", f"{out_dir}"]
            else:
                remove = ["rm", "-r", f"{out_dir}"]
            steps.append(unzip)
            steps.append(remove)
        elif out_dir.endswith(".txt"):
            mv = ["mv", f"{out_dir}", f"dataset/{out_dir}"]
            steps.append(mv)
        for step in steps:
            process = sp.Popen(step)
            process.wait()


def fetch_stopwords(data, out_dir):
    if not os.path.isdir(out_dir):
        download = ["wget", "-qO", f"{out_dir}", f"{data}"]
        unzip = ["unzip", f"{out_dir}"]
        rm = [
            "rm",
            "-r",
            f"{out_dir}",
            "554280-7e0e4a1ce04c2bb7bd41089c9821dbcf6d0c786c",
        ]
        for step in [download, unzip]:
            process = sp.Popen(step)
            process.wait()
        process = sp.Popen(
            f'mv 554280-7e0e4a1ce04c2bb7bd41089c9821dbcf6d0c786c/* {out_dir.replace("zip", "txt")}',
            shell=True,
        )
        process.wait()
        process = sp.Popen(rm)
        process.wait()


if __name__ == "__main__":
    large_dataset = "https://drive.google.com/u/0/uc?id=1mJTQbWJp-n5VAEx0dk5PeeSLo67XfbjG&confirm=t&uuid=9aff229a-d7fa-4e34-bb37-25e3923e6df0&at=AKKF8vzlclbb1yKk4JmXEjXeWIm3:1685323312377"
    small_50MB_dataset = "https://drive.google.com/u/0/uc?id=1KmVKq6_mU723EDuP-t7_ObvNn4ZdRKpv&export=download"
    stopwords_url = "https://gist.github.com/sebleier/554280/archive/7e0e4a1ce04c2bb7bd41089c9821dbcf6d0c786c.zip"
    fetch_file(large_dataset, "large_dataset.zip")
    fetch_file(small_50MB_dataset, "small_50MB_dataset.txt")
    fetch_stopwords(stopwords_url, "stopwords.zip")

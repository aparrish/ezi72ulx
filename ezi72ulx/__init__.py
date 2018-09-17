import os
from os.path import join as opj
import subprocess
import tempfile

def build_ulx(binary_path, internal_path, include_path, project_path):
    # ni
    cp = subprocess.run(
        [opj(binary_path, "ni"), "-internal", internal_path, "-project", project_path],
        encoding="utf8",
        capture_output=True,
        check=True)
    # inform6
    cp = subprocess.run([
        opj(binary_path, "inform6"),
        "-kE2SDwG",
        "+include_path="+include_path,
        opj(project_path, "Build", "auto.inf"),
        opj(project_path, "Build", "output.ulx")],
        encoding="utf8",
        capture_output=True,
        check=True)
    return opj(project_path, "Build", "output.ulx")

def build_ulx_macos(project_path, inform_app_path="/Applications/Inform.app"):
    return build_ulx(
        binary_path=opj(inform_app_path, "Contents", "MacOS"),
        internal_path=opj(
            inform_app_path, "Contents", "Resources", "Internal"),
        include_path=opj(
            inform_app_path, "Contents", "Resources", "Library", "6.11"),
        project_path=project_path)

def mk_minimal_project(path, story_source):
    os.mkdir(opj(path, "Source"))
    os.mkdir(opj(path, "Build"))
    with open(opj(path, "Source", "story.ni"), "w") as fh:
        fh.write(story_source)

def build_ulx_from_source_macos(story_source):
    with tempfile.TemporaryDirectory() as tmpdirname:
        mk_minimal_project(tmpdirname, story_source)
        output_path = build_ulx_macos(tmpdirname)
        ulx = open(output_path, "rb").read()
        return ulx


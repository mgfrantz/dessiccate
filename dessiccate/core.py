# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['run_bash', 'colab_setup', 'mkdir_if_not_exists']

# Cell
from attrdict import AttrDict
from fastcore.basics import Path
import subprocess

# Cell
def run_bash(cmd, return_output=True):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if not error:
        print(output.decode('utf-8'))
        if return_output:
            return output.decode('utf-8')
    else:
        print(error.decode('utf-8'))
        if return_output:
            return error.decoe('utf-8')

# Cell
def colab_setup():
    """
    Sets up for development in Google Colab.
    Repo must be cloned in drive/colab/ directory.
    """
    try:
        from google.colab import drive
        print('Running in colab')
        drive.mount('/content/drive', force_remount=True)
        _ = run_bash("pip install -Uqq nbdev")
        import os
        os.chdir('/content/drive/MyDrive/colab/dessiccate/')
        print("Working in", os.getcwd())
        _ = run_bash('pip install -e . --quiet')
    except:
        import os
        print("Working in", os.getcwd())
        print('Running locally')

# Cell
def mkdir_if_not_exists(self, parents=True):
    """
    Creates the directory of the path if ot doesn't exist.
    If the path is a file, will not make the file itself,
    but will create the parent directory.
    """
    if path.is_dir():
        p = path
    else:
        p = path.parent
    if not p.exists():
        p.mkdir(parents=parents)

Path.mkdir_if_not_exists = mkdir_if_not_exists
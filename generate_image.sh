#Generate Dockerfile.

#!/bin/sh

 set -e

generate_docker() {
  docker run --rm kaczmarj/neurodocker:0.6.0 generate docker \
             --base neurodebian:stretch-non-free \
             --pkg-manager apt \
             --install git num-utils gcc g++ curl build-essential nano graphviz tree \
                     git-annex-standalone nano less ncdu git-annex-remote-rclone  \
             --user=neuroscout\
             --miniconda \
                conda_install="python=3.8 nb_conda nb_conda_kernels nbconvert==6.4.5 nbformat jupyter" \
                pip_install='seaborn pyns==0.4.10 nilearn==0.8.0 altair nimare==0.0.11 pymare==0.0.2
                             jupytext==1.11.5 ghp-import jupyter-book==0.12.2 myst-nb==0.13.2 sympy==1.2
                             sphinx-book-theme jupyter_contrib_nbextensions nbval duecredit' \
                create_env='neuroscout_paper' \
                activate=true \
             --copy . /home/neuroscout/info \
             --user=root \
             --run 'chown -R neuroscout /home/neuroscout/info' \
             --run 'rm -rf /opt/conda/pkgs/*' \
             --user=neuroscout \
             --run 'mkdir -p ~/.jupyter && echo c.NotebookApp.ip = \"0.0.0.0\" > ~/.jupyter/jupyter_notebook_config.py' \
             --workdir /home/neuroscout/info/paper 
}

# generate files
generate_docker > Dockerfile
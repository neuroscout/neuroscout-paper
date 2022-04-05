<center>
<img src="https://neuroscout.org/static/Neuroscout_Simple_Wide.svg" alt="neuroscout logo" width="600" style="margin:0 0 0 0"/>
</center>

</br>
</br>

[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://neuroscout.github.io/neuroscout-paper)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/neuroscout/neuroscout-paper/HEAD)
[![GitHub size](https://img.shields.io/github/repo-size/neuroscout/neuroscout-paper)](https://github.com/neuroscout/neuroscout-paper/archive/master.zip)
[![GitHub issues](https://img.shields.io/github/issues/neuroscout/neuroscout-paper?style=plastic)](https://github.com/neuroscout/neuroscout-paper/issues)
[![GitHub PR](https://img.shields.io/github/issues-pr/neuroscout/neuroscout-paper)](https://github.com/neuroscout/neuroscout-paper/pulls)
[![License](https://img.shields.io/github/license/neuroscout/neuroscout-paper)](https://github.com/neuroscout/neuroscout-paper)




## Welcome
Within these pages we would like to provide a (interactive) walkthrough of our publication “Neuroscout: a unified platform for generalizable and reproducible fMRI research” (please check the [paper]() and the [preprint]()). This walkthrough will present the conducted analyses steps, including the used code, and allow you to rerun them and re-create the figures in an interactive manner. You can navigate through the respective sections via the `TOC` on the left side and within sections via the `TOC` on the right side. The three symbols in the top allow you to enable full screen mode, link to the underlying [Github repository](https://github.com/neuroscout/neuroscout-paper) and allow you to download the walkthrough as a `pdf` or `jupyter notebook` respectively. Some sections will additionally have a little `rocket` in that row which will allow you to interactively rerun the analyses via cloud computing, i.e. [mybinder](https://mybinder.org/). Additionally, we support public reviews and comments through an [hypothes.is](https://web.hypothes.is/) plugin with which you can interact on the right side. All of this awesomeness (talking about the infrastructure and resource) is possible through the dedicated and second to none work of the [Jupyter community](https://jupyter.org/), specifically, the [Executable/Jupyter Book](https://jupyterbook.org/intro.html) and [mybinder](https://mybinder.org/) project.

## The [Neuroscout platform](https://neuroscout.org/)

Within the above mentioned paper this resource accompanies, the [Neuroscout platform](https://neuroscout.org/) is formally introduced, with it's feasibility and usability being demonstrated via multiple analyses at the `individual dataset`/`task` and `meta-analysis` level. Specifically, a diverse set of models, including e.g. the processing of low and high-level features in both the auditory and visual domain, was run at the `individual dataset`/`task` level, followed by a `meta-analysis` across all `datasets` and `tasks`. `Code` related to `single task models` is found under [Single predictor models](https://neuroscout.github.io/neuroscout-paper/single_predictor.html) ([GitHub link](https://github.com/neuroscout/neuroscout-paper/tree/master/analyses)) / while `meta-analysis code` is found under [Meta-analyes](https://neuroscout.github.io/neuroscout-paper/meta-analyses.html) ([GitHub link](https://github.com/neuroscout/neuroscout-paper/tree/master/meta)). The `Neuroscout model IDs` for each analysis can be found in the [GitHub repository](https://github.com/neuroscout/neuroscout-paper) under /[analyses/models/](https://github.com/neuroscout/neuroscout-paper/tree/master/analyses/models).

The `analyses` are organized by `Figure` in the manuscript. Most `analyses` **require** first running `single dataset results` and then performing a `meta-analysis` for the final `figure`. You can find the notebooks to re-run the analyses and re-create the `figures` as indicated below.

- `Figure 1`

  [Individual dataset & task analyses/feature extraction methods](https://neuroscout.github.io/neuroscout-paper/analyses/)

- `Figures 3-4`

  [Individual dataset & task analyses/Single predictor models](https://neuroscout.github.io/neuroscout-paper/analyses/)

  [Meta-analyses/Single predictor models](https://neuroscout.github.io/neuroscout-paper/meta/)

- `Figure 5`

  [Individual dataset & task analyses/Face features (FaceNet) models](https://neuroscout.github.io/neuroscout-paper/analyses/)

  [Meta-analyses/Face features (FaceNet) models](https://neuroscout.github.io/neuroscout-paper/meta/)

- `Figure 6`

  [Individual dataset & task analyses/Language models](https://neuroscout.github.io/neuroscout-paper/analyses/)

  [Meta-analyses/Language models](https://neuroscout.github.io/neuroscout-paper/meta/)


## Rerunning analyses and recreating figures
There are multiple options to make use of the resources provided here. Specifically, this refers to rerunning the `analyses` and recreating the `figures`. Which one to choose heavily depends on your preference and available computational architecture.

- `Cloud computing`

   As mentioned above, sections that show the respective analyses have a little `rocket` in the top row which will allow you to interactively rerun the analyses via `cloud computing`, i.e. [mybinder](https://mybinder.org/). This is potentially the easiest option as you don't have to install/download anything. However, please note that due to restricted computing resources this option might also be the slowest in terms of rerunning the `analyses`. Instead of running a specific `analyses`, you can also easily get access to all via click the button below:

   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/neuroscout/neuroscout-paper/HEAD)

</br>

- `Software containers`   

   If you would like to rerun the `analyses` and recreate the `figures` locally on your end, you can make use of a `software container` we specifically created for this purpose. Depending on your resources, you can either use it via `Docker`:

   </br>

   ```
   docker pull neuroscout/neuroscout-paper:preprint
   ```

   or `Singularity` (works for `singularity >=2.5`):

   </br>

   ```
   singularity build neuroscout-paper-preprint.simg docker://neuroscout/neuroscout-paper:preprint
   ```


   You can then utilize as them as follows, assuming you're using `Docker`. At first you need to start the `software container` via:

   </br>

   ```
   docker run -it --rm -p 8888:8888 neuroscout-paper
   ```

   Afterwards you should be running the required `computational environment` from which you need to start a `jupyter notebook server` via:

   </br>

   ```
   jupyter-notebook --port=8888 --no-browser --ip=0.0.0.0
   ```

   which should provide you with a link that looks roughly like so (it should look slightly different on your end):

   </br>

   ```http://127.0.0.1:8888/?token=d47d101bcb9d1233471aa4fb21240ff74d520887d4c0e0b6```

   </br>

   If you click on this `link` (in your `shell`) or copy-paste it to your `browser` (NB: `Chrome` usually works best), you should
   see a `jupyter notebook server` that allows you to navigate through the provided resources, including the `analyses`. In order to rerun them, you then
   only to click on the `jupyter notebook` the `analyses` you want to rerun to open and subsequently running it.

   </br>

   (NB: the files that were used to create the `computational environment`, i.e. `software container`, can be found in the 
   [GitHub repository](https://github.com/neuroscout/neuroscout-paper) and entail a [bash script]() running [neurodocker](https://www.repronim.org/neurodocker/)
   that will write a [Dockerfile](). The latter can be used to rebuild the `software environment`.)     

## Feedback & Questions
We would highly appreciate and value every feedback, idea or question you might have. Please don’t hesitate a single second to get in touch with us. We would of course prefer if you would use the public comment function via the hypothes.is plugin (on the right side), but depending on your inquiry opening an issue in the GitHub repository would also be great.



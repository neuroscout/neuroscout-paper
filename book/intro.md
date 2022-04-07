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
Welcome! This is an interactive walkthrough of our publication “Neuroscout: a unified platform for generalizable and reproducible fMRI research”. Here you can visualize and re-run the code we used to create analyses and figures. 

In the paper, we validate the platform through some replication meta-analyses, and we showcase some more exploratory  applications that demonstrate how Neuroscout can be used to run larger-scale, more generalizable naturalistic fMRI research.

These analyses require specifying and estimating models at the level of individual datasets/tasks, and the outputs of these analyses are used as inputs to meta-analyses. This is reflected by the structure of the GitHub repository and of this book.

## Rerunning the analyses
The `analyses` follow the structure of figures in the manuscript. Most `analyses` **require** first running `single dataset results` and then performing a `meta-analysis`.
You can use this resource to simply visualize the analyses, or to rerun them and recreate the figure.

Note that, if you want to rerun meta-analyses, you do not need to rerun the dataset-level models. All statistical maps are uploaded to `NeuroVault` and can be downloaded using our meta-analysis code. If you wish to recreate and re-estimate dataset-level models, you will have to do so locally.

- `Cloud computing`

   Notebooks can be rerun on the cloud using [mybinder](https://mybinder.org/) by clicking on the `rocket` icon at the top of the notebook page. This is potentially the easiest option as you don't have to install/download anything. You can also easily access all analyses at:

   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/neuroscout/neuroscout-paper/HEAD)

</br>

- `Software containers`   

   If you want to rerun the `analyses` and recreate the `figures` locally, you can use our software containers to recreate a suitable environment. Depending on your resources, you can either use `Docker`:

   </br>

   ```
   docker pull neuroscout/neuroscout-paper:preprint
   ```

   or `Singularity` (works for `singularity >=2.5`):

   </br>

   ```
   singularity build neuroscout-paper-preprint.simg docker://neuroscout/neuroscout-paper:preprint
   ```


   If you use `Docker`, first run:

   </br>

   ```
   docker run -it --rm -p 8888:8888 neuroscout-paper
   ```

   Then, start a server via:

   </br>

   ```
   jupyter-notebook --port=8888 --no-browser --ip=0.0.0.0
   ```

   which should provide you with a link that looks roughly like this:

   </br>

   ```http://127.0.0.1:8888/?token=d47d101bcb9d1233471aa4fb21240ff74d520887d4c0e0b6```

   </br>

   If you click on this link or copy-paste it in your browser, you should
   see a `jupyter notebook server` that allows you to navigate these resources.

   </br>

## Feedback & Questions
If you have any feedback, don't hesitate to get in touch!
We also support public reviews and comments through an [hypothes.is](https://web.hypothes.is/) plugin with, which you can interact by clicking on the arrow at the top right side of the page.
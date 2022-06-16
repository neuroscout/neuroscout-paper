<center>
<img src="https://neuroscout.org/static/neuroscout_simpler_dark_blue_medium.svg" alt="neuroscout logo" width="600" style="margin:0 0 0 0"/>
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

In the paper, we validate the [Neuroscout platform](https://neuroscout.org/) by replicating established effects from cognitive neuroscience using automatically extracted features in over 30 naturalistic datasets. We then use `meta-analysis` to synthesize single dataset findings, resulting in most robust and generalize estimates. In addition, we also showcase more exploratory applications in two domains (`face processing` & `natural language perception`) that demonstrate how `Neuroscout` can be used to run more generalizable naturalistic `fMRI` research.

These analyses require specifying and estimating models at the level of `individual datasets/tasks`, and the outputs of these analyses are used as inputs to `meta-analyses`. This is reflected by the structure of the [GitHub repository](https://github.com/neuroscout/neuroscout-paper) and of this book.

## Re-running the analyses
The `analyses` follow the structure of figures in the manuscript. Most `analyses` **require** first running `single dataset results` (using `Neuroscout`) and then performing a `meta-analysis` (using `NiMARE`).
You can use this resource to simply visualize the analyses, or to re-run them and recreate the figure.

Note that, if you want to re-run meta-analyses, you do not need to re-run the dataset-level models. All statistical maps are uploaded to `NeuroVault` and can be downloaded using our meta-analysis code. If you wish to recreate and re-estimate dataset-level models, you will have to do so locally.

- `Cloud computing`

   `Notebooks` can be re-run on the cloud using [mybinder](https://mybinder.org/) by clicking on the `rocket` icon at the top of the notebook page. This is potentially the easiest option as you don't have to install/download anything. You can also easily access all analyses at:

   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/neuroscout/neuroscout-paper/HEAD)

</br>

- `Software containers`   

   If you want to re-run the `analyses` and recreate the `figures` locally, you can use our `software containers` to recreate a suitable environment. More precisely, you can obtain the corresponding `Docker image` via:

   </br>

   ```
   docker pull neuroscout/neuroscout-paper:preprint
   ```

   and then start it:

   </br>

   ```
   docker run -it --rm -p 8888:8888 neuroscout-paper
   ```

   Subsequently, start a `jupyter notebook server` via:

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

- `local python environment`

   Finally, if you want to re-run `analyses` and re-create `figures` locally without `sotware containers`, you can do so via using a `python environment`. For this to work, you initially need to download the repository with the `notebooks` and other necessary files from [GitHub](https://github.com/neuroscout/neuroscout-paper). 
   
   It is recommend to create a new `python environment` through e.g. `conda` to avoid installation and dependencies issues. For example:

   </br>

   ```
   conda create -n neuroscout_analyses python==3.8
   ```
   
   </br>

   which you then can `activate` and after navigating to the downloaded repository, install the required `libraries` via:

   </br>

   ```
   conda activate neuroscout_analyses
   cd /path/to/neuroscout-paper
   pip install -r requirements.txt
   ```

   </br>

   (NB: you need to run the above code line-by-line and exchange the `/path/to` part above to the `path` you downloaded the `neuroscout-paper` repository to.)

   Subsequently, start a `jupyter notebook server` via:

   </br>

   ```
   jupyter-notebook
   ```

   which should provide you with a link that looks roughly like this:

   </br>

   ```http://127.0.0.1:8888/?token=d47d101bcb9d1233471aa4fb21240ff74d520887d4c0e0b6```

   </br>

   If you click on this link or copy-paste it in your browser, you should
   see a `jupyter notebook server` that allows you to re-run the `analyses` and re-create the `figures` through the dedicated `python environment` created above.

   </br>

## Feedback & Questions
If you have any feedback, don't hesitate to get in touch!
We also support public reviews and comments through an [hypothes.is](https://web.hypothes.is/) plugin with, which you can interact by clicking on the arrow at the top right side of the page.

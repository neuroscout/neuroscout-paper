# neuroscout-paper

This repository contains the analysis code for the analyses in the manuscript: "Neuroscout: a unified platform for generalizable and reproducible fMRI research"

Analyses in the paper required running models at the individual dataset / task level, following by a meta-analysis across all datasets and tasks. Code related to single task models is found in `analyses/` while meta-analysis code is found in `/meta`. The Neuroscout model IDs for each analysis can be found under `/analyses/models/`. 

The analyses are organized by Figure in the manuscript. Most analyses requires first running single dataset results and then performing a meta-analysis for the final figure. In the top level directory, you can find the notebooks to create and 

*Figure 1*

[analyses/0-figure_1_methods.ipynb](https://github.com/neuroscout/neuroscout-paper/tree/master/book/analyses/0-figure_1_methods.ipynb)

*Figures 3-4*

[analyses/1-single_predictor_models.ipynb](https://github.com/neuroscout/neuroscout-paper/tree/master/book/analyses/1-single_predictor_models.ipynb)

[meta/1-single_predictor_models.ipynb](https://github.com/neuroscout/neuroscout-paper/tree/master/book/meta/1-single_predictor_models_meta.ipynb)

*Figure 5*

[analyses/2-face_features.ipynb](https://github.com/neuroscout/neuroscout-paper/tree/master/book/analyses/2-face_features.ipynb)

[meta/2-face_features.ipynb](https://github.com/neuroscout/neuroscout-paper/tree/master/book/meta/2-face_features_meta.ipynb)

*Figure 6*

[analyses/3-language_features.ipynb](https://github.com/neuroscout/neuroscout-paper/tree/master/book/analyses/3-language_features.ipynb)

[meta/3-language_features.ipynb](https://github.com/neuroscout/neuroscout-paper/tree/master/book/meta/3-language_features_models.ipynb)

---
**NOTE**

Some of the outputs from Jupyter notebooks cells may not render correctly on Github.
You can visualize them on our Jupyter book: https://neuroscout.github.io/neuroscout-paper/ (or pasting their url on https://nbviewer.org/).
---
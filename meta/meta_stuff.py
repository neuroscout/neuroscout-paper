from pathlib import Path
import re
from collections import defaultdict
import json
import warnings
import os

warnings.filterwarnings("ignore")
from itertools import chain

import pymare as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

from nimare.dataset import Dataset
from nimare.io import convert_neurovault_to_dataset
from nimare.meta import ibma
import nibabel as nb
from pyns import Neuroscout
from nilearn.datasets import load_mni152_template
from nilearn.image import resample_to_img
from nilearn import masking
import nilearn.plotting as plotting


def create_dset(
    effect,
    neuroscout_ids,
    map_types=["variance", "univariate-beta map"],
    name=None,
    overwrite=False,
    camel_case=True,
):
    """Download maps from NeuroVault and save them locally,
    along with relevant metadata from NeuroScout."""

    #  Make directories if needed
    analysis_dir = Path("./analyses")
    analysis_dir.mkdir(exist_ok=True)
    ds_dir = Path("./datasets")
    ds_dir.mkdir(exist_ok=True)
    # ma_dir = Path('./ma-maps')
    # ma_dir.mkdir(exist_ok=True)

    ns = Neuroscout()
    nv_colls = {}

    for id_ in neuroscout_ids:

        filename = analysis_dir / f"{id_}.json"
        if filename.exists() and not overwrite:
            analysis = json.load(open(filename, "r"))
        else:
            analysis = ns.analyses.get_full(id_)
            json.dump(analysis, open(filename, "w"))

        if not analysis.get("neurovault_collections"):
            continue

        nv_colls[analysis["hash_id"]] = analysis["neurovault_collections"][-1]["collection_id"]

    mask_img = masking.compute_gray_matter_mask(load_mni152_template())

    dset = convert_neurovault_to_dataset(
        nv_colls,
        {snake_to_camel(effect): snake_to_camel(effect)},
        img_dir=str(Path("./images").absolute()),
        mask=mask_img,
    )

    dset.save(ds_dir / f"{effect}_dset.pkl")

    return dset


def snake_to_camel(text):
    """Convert snake_case to camelCase--needed when downloading some NV images."""
    cc = "".join(x.capitalize() or "_" for x in text.split("_"))
    cc = re.sub("([\.\-])(\w)", lambda x: x.group(1) + x.group(2).capitalize(), cc)
    return cc[0].lower() + cc[1:]


def process_set(
    name,
    effects=None,
    json_data=None,
    analyze=True,
    analysis_method="nimare",
    download=True,
    plot=True,
    camel_case=True,
    overwrite=False,
    stat="z",
    exclude=None,
    analysis_kwargs=None,
    plot_kwargs=None,
    save_maps=True,
):

    if analysis_kwargs is None:
        analysis_kwargs = {}

    if plot_kwargs is None:
        plot_kwargs = {}

    # Retrieve data if needed
    if json_data is not None:
        if isinstance(json_data, str):
            json_data = requests.get(json_data).json()

        # Build dict of effects --> analysis IDs
        effects = defaultdict(list)
        hash_lookup = {}
        for c, dsets in json_data.items():
            hash_lookup[c] = {}
            for ds, children in dsets.items():
                effects[c].extend(children.values())
                for movie, hash_ in children.items():
                    hash_lookup[c][hash_] = movie

    # Download maps
    dsets = {}
    if download:
        for effect, ids in effects.items():
            print(f"Downloading maps for effect '{effect}'...")
            dsets[effect] = create_dset(
                effect, ids, name=name, overwrite=overwrite, camel_case=camel_case
            )

    else:
        dsets = {effect: Dataset.load(f"./datasets/{effect}_dset.pkl") for effect in effects}

    if analyze:
        fx_names = sorted(list(effects.keys()))
        if exclude is not None:
            analysis_dir = Path("./analyses")

            def filter_analyses(ids):
                filtered_ids = []
                for id_ in ids:
                    a_id = re.search("study-(\w{5})-.*", str(id_)).group(1)
                    filename = analysis_dir / f"{a_id}.json"
                    # Ugh
                    if not filename.exists():
                        filename = analysis_dir / f"{a_id} (Case Conflict).json"
                    analysis = json.load(open(filename, "r"))
                    if analysis["model"]["Input"]["Task"] not in exclude:
                        filtered_ids.append(id_)
                return filtered_ids

            dsets = {
                effect: dset.slice(filter_analyses(dset.ids)) for effect, dset in dsets.items()
            }

        meta_results = {
            effect: ibma.DerSimonianLaird(resample=True).fit(dset) for effect, dset in dsets.items()
        }
        eff_imgs = [meta_results[fx].get_map(stat) for fx in sorted(list(meta_results.keys()))]
        for fx_name in fx_names:
            print(
                (
                    f"meta-analyzing {len(meta_results[fx_name].estimator.inputs_['id'])}"
                    f" studies for effect: {fx_name}"
                )
            )

        if save_maps:
            ma_dir = Path("./ma-maps")
            ma_dir.mkdir(exist_ok=True)
            for i, fxn in enumerate(fx_names):
                ma_path = Path(".") / "ma-maps" / (name + "-" + fxn + ".nii.gz")
                eff_imgs[i].to_filename(ma_path)

        if plot:
            # Big ol' plot
            n_eff = len(fx_names)
            fig, axes = plt.subplots(n_eff, 1, figsize=(14, n_eff * 2.5))
            if n_eff == 1:
                axes = [axes]
            defaults = dict(
                threshold=3.3,
                vmax=None,
                display_mode="z",
                cut_coords=[-24, -12, 0, 12, 24, 36, 48, 60],
            )
            defaults.update(plot_kwargs)
            for i, img in enumerate(eff_imgs):
                plotting.plot_stat_map(img, axes=axes[i], title=fx_names[i], **defaults)

    return eff_imgs

if __name__ == '__main__':
    import os
    os.chdir('./meta')
    json_data = {"speech": {"Sherlock": {"sherlockPart1": "wK3Op"}, "HealthyBrainNetwork": {"movieDM": "AobKG"}, "SherlockMerlin": {"MerlinMovie": "Ar6VO", "SherlockMovie": "MzqbZ"}, "Life": {"life": "Adp4e"}, "Raiders": {"raiders": "M8LX1"}, "SchematicNarrative": {"perception": "AVr83"}, "studyforrest": {}, "ParanoiaStory": {"story": "A1GkD"}, "LearningTemporalStructure": {"movie": "MNQ0q"}, "Budapest": {"movie": "w0gBX"}}, "rms": {"Sherlock": {"sherlockPart1": "MXmd3"}, "HealthyBrainNetwork": {"movieDM": "AbnRy"}, "SherlockMerlin": {"MerlinMovie": "MnPpP", "SherlockMovie": "wWV8y"}, "Life": {"life": "9EWBK"}, "Raiders": {"raiders": "MGbQj"}, "SchematicNarrative": {"perception": "AqbR8"}, "studyforrest": {"movie": "Maqy1"}, "ParanoiaStory": {"story": "wjv20"}, "LearningTemporalStructure": {"movie": "9Lq1z"}, "Budapest": {"movie": "wK2Np"}}, "text": {"Sherlock": {"sherlockPart1": "AxkEK"}, "HealthyBrainNetwork": {"movieDM": "wJJo4"}, "SherlockMerlin": {"MerlinMovie": "M34zo", "SherlockMovie": "AYX8e"}, "Life": {"life": "9BbP5"}, "Raiders": {"raiders": "MDzYd"}, "SchematicNarrative": {"perception": "wQo1d"}, "studyforrest": {"movie": "w0vpX"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "wK3vp"}, "Budapest": {"movie": "AopLG"}}, "brightness": {"Sherlock": {"sherlockPart1": "AobEG"}, "HealthyBrainNetwork": {"movieDM": "A6m1k"}, "SherlockMerlin": {"MerlinMovie": "wly2W", "SherlockMovie": "AxkE1"}, "Life": {"life": "wJJoe"}, "Raiders": {"raiders": "M34zR"}, "SchematicNarrative": {"perception": "AYX8P"}, "studyforrest": {"movie": "9BbPN"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "MDzYD"}, "Budapest": {"movie": "Arq4O"}}, "shot_change": {"Sherlock": {"sherlockPart1": "wQo3W"}, "HealthyBrainNetwork": {"movieDM": "w0vPv"}, "SherlockMerlin": {"MerlinMovie": "wK3V2", "SherlockMovie": "AobXB"}, "Life": {"life": "Ar6N0"}, "Raiders": {"raiders": "MzqP1"}, "SchematicNarrative": {"perception": "Adpkx"}, "studyforrest": {"movie": "M8Lpl"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "AVr0K"}, "Budapest": {"movie": "MzQpZ"}}, "any_faces": {"Sherlock": {"sherlockPart1": "A1GoO"}, "HealthyBrainNetwork": {"movieDM": "wOVxB"}, "SherlockMerlin": {"MerlinMovie": "MXmod", "SherlockMovie": "AbnkR"}, "Life": {}, "Raiders": {"raiders": "MnPXX"}, "SchematicNarrative": {"perception": "wWVKQ"}, "studyforrest": {"movie": "9EWVr"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "MGbVD"}, "Budapest": {}}, "hand": {"Sherlock": {"sherlockPart1": "Aqbq3"}, "HealthyBrainNetwork": {"movieDM": "Maqmb"}, "SherlockMerlin": {"MerlinMovie": "wjv7m", "SherlockMovie": "9LqeK"}, "Life": {"life": "97v1Q"}, "Raiders": {"raiders": "wkKRD"}, "SchematicNarrative": {"perception": "M4ndy"}, "studyforrest": {"movie": "A2YrP"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "MNWl0"}, "Budapest": {"movie": "AdR1e"}}, "action": {"Sherlock": {"sherlockPart1": "M5Qpn"}, "HealthyBrainNetwork": {"movieDM": "9eKPb"}, "SherlockMerlin": {"MerlinMovie": "AZy5W", "SherlockMovie": "Mvb7R"}, "Life": {"life": "MmvkX"}, "Raiders": {"raiders": "Mp8Xj"}, "SchematicNarrative": {"perception": "wyD7W"}, "studyforrest": {"movie": "MR2Yb"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "wgjG0"}, "Budapest": {"movie": "M8vd1"}}, "landscape": {"Sherlock": {"sherlockPart1": "MPKJL"}, "HealthyBrainNetwork": {"movieDM": "A6m5k"}, "SherlockMerlin": {"MerlinMovie": "wly7W", "SherlockMovie": "Axk71"}, "Life": {"life": "wJJ1e"}, "Raiders": {"raiders": "M34dR"}, "SchematicNarrative": {"perception": "AYXrP"}, "studyforrest": {"movie": "9BbON"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "MDzgD"}, "Budapest": {"movie": "AVjJ3"}}, "building": {"Sherlock": {"sherlockPart1": "wQoxW"}, "HealthyBrainNetwork": {"movieDM": "w0vov"}, "SherlockMerlin": {"MerlinMovie": "wK3W2", "SherlockMovie": "Aob3B"}, "Life": {"life": "Ar6D0"}, "Raiders": {"raiders": "Mzql1"}, "SchematicNarrative": {"perception": "AdpDx"}, "studyforrest": {"movie": "M8LYl"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "AVrDK"}, "Budapest": {"movie": "A13DD"}}, "indoors": {"Sherlock": {"sherlockPart1": "A1GPO"}, "HealthyBrainNetwork": {"movieDM": "wOV6B"}, "SherlockMerlin": {"MerlinMovie": "MXm0d", "SherlockMovie": "AbnYR"}, "Life": {"life": "MnPJX"}, "Raiders": {"raiders": "wWVQQ"}, "SchematicNarrative": {"perception": "9EWXr"}, "studyforrest": {"movie": "MGbeD"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "AqbB3"}, "Budapest": {"movie": "wOOv3"}}, "city": {"Sherlock": {"sherlockPart1": "Maq3b"}, "HealthyBrainNetwork": {"movieDM": "wjvzm"}, "SherlockMerlin": {"MerlinMovie": "9LqXK", "SherlockMovie": "97v3Q"}, "Life": {"life": "wkK6D"}, "Raiders": {"raiders": "M4nly"}, "SchematicNarrative": {"perception": "A2YzP"}, "studyforrest": {"movie": "MNWX0"}, "ParanoiaStory": {}, "LearningTemporalStructure": {"movie": "M5Qxn"}, "Budapest": {"movie": "MXjY3"}}, "animal": {"HealthyBrainNetwork": {"movieDM": "MpDX5"}, "SchematicNarrative": {"perception": "wy27p"}, "studyforrest": {"movie": "MRaYy"}, "Raiders": {"raiders": "wgyGL"}, "Life": {"life": "MPqJ4"}, "ParanoiaStory": {}, "Sherlock": {"sherlockPart1": "A6oJv"}, "SherlockMerlin": {"MerlinMovie": "wl8Py", "SherlockMovie": "AxBzB"}, "LearningTemporalStructure": {"movie": "wJ3PG"}, "Budapest": {"movie": "AbqEy"}}, "music": {"HealthyBrainNetwork": {"movieDM": "M376v"}, "SchematicNarrative": {"perception": "AYyKz"}, "studyforrest": {"movie": "9Bqnv"}, "Raiders": {"raiders": "MD1vN"}, "Life": {"life": "wQDxq"}, "ParanoiaStory": {}, "Sherlock": {"sherlockPart1": "w0go1"}, "SherlockMerlin": {"MerlinMovie": "wK2Wx", "SherlockMovie": "Aop3K"}, "LearningTemporalStructure": {"movie": "A6oJ1"}, "Budapest": {"movie": "MnkeP"}}, "vehicle": {"HealthyBrainNetwork": {"movieDM": "wl8P7"}, "SchematicNarrative": {"perception": "AxBzz"}, "studyforrest": {"movie": "wJ3Px"}, "Raiders": {"raiders": "M376J"}, "Life": {"life": "AYyKg"}, "ParanoiaStory": {}, "Sherlock": {"sherlockPart1": "9BqnV"}, "SherlockMerlin": {"MerlinMovie": "MD1vE", "SherlockMovie": "wQDx8"}, "LearningTemporalStructure": {"movie": "w0gol"}, "Budapest": {"movie": "wWyry"}}, "water": {"HealthyBrainNetwork": {"movieDM": "wK2WX"}, "SchematicNarrative": {"perception": "Aop36"}, "studyforrest": {"movie": "ArqDR"}, "Raiders": {"raiders": "MzQlJ"}, "Life": {"life": "AdRDV"}, "ParanoiaStory": {}, "Sherlock": {"sherlockPart1": "M8vY4"}, "SherlockMerlin": {"MerlinMovie": "AVjDO", "SherlockMovie": "A13PN"}, "LearningTemporalStructure": {"movie": "wOO65"}, "Budapest": {"movie": "9EdZK"}}, "wood": {"HealthyBrainNetwork": {"movieDM": "MXj0J"}, "SchematicNarrative": {"perception": "AbqY4"}, "studyforrest": {"movie": "MnkJ8"}, "Raiders": {"raiders": "wWyQZ"}, "Life": {"life": "9EdX1"}, "ParanoiaStory": {}, "Sherlock": {"sherlockPart1": "MGveo"}, "SherlockMerlin": {"MerlinMovie": "AqQBj", "SherlockMovie": "Ma432"}, "LearningTemporalStructure": {"movie": "wjNzL"}, "Budapest": {"movie": "MGvmj"}}, "tool": {"HealthyBrainNetwork": {"movieDM": "9L2XR"}, "SchematicNarrative": {"perception": "97p3z"}, "studyforrest": {"movie": "wkV62"}, "Raiders": {"raiders": "M4jlO"}, "Life": {"life": "A2542"}, "ParanoiaStory": {}, "Sherlock": {"sherlockPart1": "MNQBW"}, "SherlockMerlin": {"MerlinMovie": "M5545", "SherlockMovie": "9ey74"}, "LearningTemporalStructure": {"movie": "AZ47m"}, "Budapest": {}}, "people": {"HealthyBrainNetwork": {"movieDM": "AZ4qk"}, "SchematicNarrative": {"perception": "Mv382"}, "studyforrest": {"movie": "Mm3BB"}, "Raiders": {"raiders": "MpDP5"}, "Life": {"life": "wy2Op"}, "ParanoiaStory": {}, "Sherlock": {"sherlockPart1": "MRa1y"}, "SherlockMerlin": {"MerlinMovie": "wgy6L", "SherlockMovie": "MPq84"}, "LearningTemporalStructure": {"movie": "A6o8v"}}}
    nimare_imgs = process_set('visual', json_data=json_data, download=True, exclude=['SherlockMovie'])

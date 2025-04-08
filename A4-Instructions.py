# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Background
#
# This assignment is a continuation of Assignment 3, using forward models. 
# Use the same dataset and Python environment.
#
# The same resources may be helpful:
# - Eelbrain [examples on TRFs](https://eelbrain.readthedocs.io/en/latest/auto_examples/#temporal-response-functions), in particular [TRF for Alice EEG Dataset](https://eelbrain.readthedocs.io/en/latest/auto_examples/temporal-response-functions/alice-trf.html)
# - Paper describing more background: https://elifesciences.org/articles/85012

# ## General instructions
#
# Same general instructions as for A3, with one exception:
#
# To speed up the analysis:
# - It's okay to perform the analysis at 50 Hz (with a 20 Hz low pass filter).
# - It is okay to save TRFs on disk so you can get back to your result without re-estimating models.
#   In an earlier part in your notebook, you can save the TRFs as `*.pickle` files 
#   (see [eelbrain.save.pickle](https://eelbrain.readthedocs.io/en/latest/generated/eelbrain.save.pickle.html)),
#   and in a later part of your script, you can load them again.

# ## Setup
#
# Setup is based on the [Alice repository](https://github.com/Eelbrain/Alice) and data, as used in Assignment 3.

# ## 1.
#
# Question: Does brain activity represent the envelope of acoustic power, acoustic onsets (edges), or both?
#
# Use acoustic envelope and onset predictors based on the sound wave, as shown in the 
# [example](https://eelbrain.readthedocs.io/en/latest/auto_examples/temporal-response-functions/alice-trf.html). 
#
# ### Approach: evaluating models
#
# Implement a group level evaluation of the model fits. 
#
# You want to test the predictive power of a given predictor, 
# while controlling for the predctive power of a second predictor.
# A general strategy for this is to fit a full model (all predictors) 
# and a reduced model (leaving out one of the predictors),
# and compare predictive power between the two.
# Make sure to use cross-validation with an unseen test set 
# (through setting the relevant 
# [`boosting`](https://eelbrain.readthedocs.io/en/latest/generated/eelbrain.boosting.html) parameter).
# Use the `BoostingResult.proportion_explained` attribute as measure of predictive power.
#
# For statistics, use a mass-univariate tests, taking into account all sensors. 
# Mass-univariate tests are described in these two examples:
#
# - [Permutation statistics](https://eelbrain.readthedocs.io/en/latest/auto_examples/mass-univariate-statistics/permutation-statistics.html)
# - [T-test](https://eelbrain.readthedocs.io/en/latest/auto_examples/mass-univariate-statistics/sensor-ttest.html)

# ## 2.
#
# Question: Is the cochleagram a better predctor of brain actiity than the acoustic waveform?
#
# ### Approach: Cochleagrams
#
# Generate predictors reflecting the acoustic envelope and acoustic onsets based on the cochleagrams.
# For speed, and comparability, you can use one-dimensional time series by summing across frequency bands.
#
# There are scripts provided in the [Alice repository](https://github.com/Eelbrain/Alice) showing how
# to create these gammatone predictors (`make_gammatone.py` and `make_gammatone_predictors.py` in the 
# [`Alice/predictors`](https://github.com/Eelbrain/Alice/blob/main/predictors) directory).
# You can use those scripts and just load the resulting predictors in your notebook.

# ## 3: Bonus
#
# Think of a predictor variable that could further improve 
# the prediction of EEG responses over the predictors from **2**.
# Explain why you think it could improve predictions.
# Test whether, in fact, it does.
#
# Evaluation will rely on your reasoning, not on whether your result is significant.
# I.e., if you provide an interesting hypothesis, 
# the points you get will not depend on whether the outcome is significant or not.
#
# You are allowed to use the variables in 
# `'Alice/stimuli/AliceChapterOne-EEG.csv'`,
# which are described in the original paper on the dataset
# ([Brennan & Hale, 2019](https://doi.org/10.1371/journal.pone.0207741))
# and the dataset [readme](https://deepblue.lib.umich.edu/data/concern/data_sets/bg257f92t#read_me_display).
#

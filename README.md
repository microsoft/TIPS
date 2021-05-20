# TIPS: 
[**Tasks**](#tasks) |
[**Dataset**](#get-dataset) |
[**Evaluation**](#Evaluation)

## Introduction
This repository contains information about the Video Procedure Segmentation evaluation benchmark TIPS.

TIPS contains 63k videos and more than 300k procedure segments and 8000 hours from instructional videos on Youtube, which covers plenty of how-to areas such as cooking, health, beauty, parenting, gardening, etc. Comparing to other temporal video segmentation datasets, TIPS has 4 characteristics: (1) Scale. TIPS is the largest temporal video segmentation dataset, and more specifically, the largest video procedure segmentation dataset. (2) Diversity. TIPS contains open-domain instructional videos on Youtube including cooking, health, beauty, parenting, gardening, etc. (3)Continuity. Note that the segments in TIPS are continuous, while the segments in Youcook2 are incontinuous. The continuous segmentation can easily overview the procedure of the whole video structure globally. (4) Auto-generated. We introduce a workflow to auto-generate the TIPS dataset from Youtube with guratee of high quality. With the increase of videos uploaded to Youtube, it is feasible to collect more data automatically in the future. 

## Tasks
TIPS targets on Video Procedure Segmentation Task (VPS).

## Get Dataset
In order to use our dataset, please navigate to [TIPS Dataset](./dataset).

## Evaluation
To evaluate your model's performance, we will compare your prediction files with the ground truth file.
We are keeping our evaluation data held out, to evaluate your performance, please use the following command: 

```
python EIoU_Evaluation.py --prediction_dir <prediction_files_folder> --ground_truth_file <ground_truth_file>
```
The detailed format of each task is at [Evaluation ReadMe](./evaluation/README.md).

# License and Legal Notice
We release the TIPS dataset (under https://github.com/microsoft/TIPS ) under the following Open Use of Data Agreement ([LICENSE](https://github.com/microsoft/Open-Use-of-Data-Agreement)). By downloading this dataset and the contents, you are automatically agreeing to accept the use terms.

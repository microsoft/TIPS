# TIPS: 
[**Tasks**](#tasks) |
[**Dataset**](#get-dataset) |
[**Evaluation**](#Evaluation) |
[**Baseline**](#get-Baseline) 

## Introduction
This repository contains information about the Video Procedure Segmentation evaluation benchmark TIPS.

TIPS contains 63k videos and more than 300k procedure segments and 8000 hours from instructional videos on Youtube, which covers plenty of how-to areas such as cooking, health, beauty, parenting, gardening, etc. Comparing to other temporal video segmentation datasets, TIPS has 4 characteristics: (1) Scale. TIPS is the largest temporal video segmentation dataset, and more specifically, the largest video procedure segmentation dataset. (2) Diversity. TIPS contains open-domain instructional videos on Youtube including cooking, health, beauty, parenting, gardening, etc. (3)Continuity. Note that the segments in TIPS are continuous, while the segments in Youcook2 are incontinuous. The continuous segmentation can easily overview the procedure of the whole video structure globally. (4) Auto-generated. We introduce a workflow to auto-generate the TIPS dataset from Youtube with guratee of high quality. With the increase of videos uploaded to Youtube, it is feasible to collect more data automatically in the future. 

## Tasks
TIPS targets on Video Procedure Segmentation Task (VPS).

## Get Dataset
In order to use our dataset, please navigate to [TIPS Leaderboard](https://microsoft.github.io/TIPS/) and agree to our terms of service. After you do so a download link will be made available.

## Get Baseline
We put the baseline system to [MT-GBD](https://github.com/microsoft/mt_gbd) repo. It contains a baseline model that are trained based on TIPS.

## Leaderboard Submission

## Evaluation
To evaluate your model's performance, we will compare your prediction files with the ground truth file.
We are keeping our evaluation data held out, to evaluate your performance, please use the following command: 

```
python EIoU_Evaluation.py --prediction_dir <prediction_files_folder> --ground_truth_file <ground_truth_file>
```
The detailed format of each task is at [Evaluation ReadMe](./evaluation/README.md).

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.

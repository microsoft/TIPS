# XGLUE: 
[**Tasks**](#tasks-and-languages) |
[**Dataset**](#get-dataset) |
[**Leaderboard**](https://microsoft.github.io/XGLUE/) |
[**Baseline**](https://github.com/microsoft/Unicoder) |
[**Paper**](https://arxiv.org/abs/2004.01401)

## Introduction
This repository contains information about the cross-lingual evaluation benchmark XGLUE, which is composed of 11 tasks spans 19 languages.
For each task, the training data is only available in English. This means that to succeed at XGLUE, a model must have a strong zero-shot cross-lingual transfer capability to learn from the English data of a specific task and transfer what it learned to other languages. 
Comparing to its concurrent work XTREME, XGLUE has two characteristics: First, it includes cross-lingual NLU and cross-lingual NLG tasks at the same time; 
Second, besides including 5 existing cross-lingual tasks (i.e. NER, POS, MLQA, PAWS-X and XNLI), XGLUE selects 6 new tasks from Bing scenarios as well, 
including News Classification (NC), Query-Ad Matching (QADSM), Web Page Ranking (WPR), QA Matching (QAM), Question Generation (QG) and News Title Generation (NTG). 
Such diversities of languages, tasks and task origin provide a comprehensive benchmark for quantifying the quality of a pre-trained model on cross-lingual natural language understanding and generation. 

The 11 tasks in XGLUE:

![](./xglue_overview1.png)

The 19 languages in XGLUE, including Arabic (ar), Bulgarian (bg), German (de), Greek (el), English (en), Spanish (es), French (fr), Hindi (hi), Italian (it), Dutch (nl), Polish (pl), Portuguese (pt), Russian (ru), Swahili (sw), Thai (th), Turkish (tr), Urdu (ur), Vietnamese (vi) and Chinese (zh):

![](./xglue_overview2.png)

## Tasks and Languages
The task in TIPS c

## Get Dataset
In order to use our dataset, please navigate to [TIPS Leaderboard](https://microsoft.github.io/TIPS/) and agree to our terms of service. After you do so a download link will be made available.

## Get Baseline
We put the baseline system to [MT-GBD](https://github.com/microsoft/mt_gbd) repo. It contains a baseline model that are trained based on TIPS.

## Leaderboard Submission
### Submissions
To submit your predictions for evaluation, please create a single folder which contains the 11 sub-folders named after each task (see [reference file](evaluation/Unicoder_prediction_on_XGLUE_test) for an example). 
Inside each folder, create one prediction file for each language and name the file using the following format: `{language}.prediction` where `{language}` is the 2 character [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code.
Please validate that you have done this correctly by evaluating against the development file. Once that is done <a href='xglue@microsoft.com'>email your submission</a>. We will reply with your model performance.

### Evaluation
To evaluate your model's performance, we will compare your prediction files with the ground truth files.
We are keeping our evaluation data held out, to evaluate your performance, please use the following command: 

```
python EIoU_Evaluation.py --prediction_dir <prediction_files_folder> --ground_truth_file <ground_truth_file>
```

This file has several dependencies:

```
argparse
```

The detailed format of each task is at [Evaluation ReadMe](./evaluation/README.md).
### Baseline
To aid your model comparison we have included the output of our baseline system, unicoder.  Please find the [dev example](evaluation/Unicoder_prediction_on_XGLUE_dev) and [test example](evaluation/Unicoder_prediction_on_XGLUE_test).
## Paper
If you use our benchmark or dataset, please cite our paper `\cite{Liang2020XGLUEAN}`.

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

# Evaluation
We will use following command to evaluate your model's performance on test dataset: 
```
python EIoU_Evaluation.py --prediction_dir <prediction_files_folder> --ground_truth_file <ground_truth_file>
```
ground_truth_file is tips.tvs.test.tsv under dataset.

# prediction file format
file should be ended with .prediction, for each line the format is:
url \t stepid \t predict_start_second \t predict_end_second 
(predict_start_second, predict_end_second should be integer)

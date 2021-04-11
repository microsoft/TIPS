import argparse
import os
from os.path import isfile, join
from os import listdir

parser = argparse.ArgumentParser()
parser.add_argument(
        "--prediction_dir",
        default=None,
        type=str,
        required=True,
        help="The prediction data dir. Should contain the .tsv files (or other data files) for the task.",
)

parser.add_argument(
        "--ground_truth_file",
        default=None,
        type=str,
        required=True,
        help="The ground truth data file",
)




def iou_calucate(in_groundtruth,in_predict):
    #[a,b][c,d]

    #print(in_groundtruth)

    a = in_groundtruth[0]
    b = in_groundtruth[1] 
    c = in_predict[0]
    d = in_predict[1]
    
    #c d a b
    #a b c d
    if((d <= a) | (b <= c)):
        return 0

    #c a d b
    elif((c <= a) & (d <= b)):
        a_and_b = d - a
        a_or_b = b - c
    #a c d b
    elif((a <= c) & (d <= b)):
        a_and_b = d - c
        a_or_b = b - a
    
    #a c b d
    elif((a <= c) & (b <= d)):
        a_and_b = b - c
        a_or_b = d - a
    
        #c a b d
    elif((c <= a) & (b <= d)):
        a_and_b = b - a
        a_or_b = d - c
    else:
        print("error")
        print(a,b,c,d)

    return a_and_b / a_or_b
def maxov_calucate(in_groundtruth,in_predict):
    #[a,b][c,d]

    #print(in_groundtruth)

    a = in_groundtruth[0]
    b = in_groundtruth[1] 
    c = in_predict[0]
    d = in_predict[1]
    
    #1.  c d a b c d
    if((d <= a) | (b <= c)):
        return 0
    #2.  c a d b
    elif((c <= a) & (d <= b)):
        max_overlap = b - c
        return max_overlap
    #3.  a c d b
    elif((a <= c) & (d <= b)):
        max_overlap = b - a
        return max_overlap

     #4.  a c b d
    elif((a <= c) & (b <= d)):
        max_overlap = d - a
        return max_overlap
    
        #5.  c a b d
    elif((c <= a) & (b <= d)):
        max_overlap = d - c
        return max_overlap
    else:
        print("error")
        print(a,b,c,d)
        return a_or_b

    return a_or_b
def minov_calucate(in_groundtruth,in_predict):
    #[a,b][c,d]

    #print(in_groundtruth)

    a = in_groundtruth[0]
    b = in_groundtruth[1] 
    c = in_predict[0]
    d = in_predict[1]
    
    #c d a b c d
    if((d <= a) | (b <= c)):
        return 0
    #c a d b
    elif((c <= a) & (d <= b)):
        min_overlap = d - a
        return min_overlap
    #a c d b
    elif((a <= c) & (d <= b)):
        min_overlap = d - c
        return min_overlap

    elif((a <= c) & (b <= d)):
        min_overlap = b - c
        return min_overlap

    
        #c a b d
    elif((c <= a) & (b <= d)):
        min_overlap = b - a
        return min_overlap
    else:
        print("error")
        print(a,b,c,d)

    return 0


def miou_v3_linear_clean(in_video_groundtruth,in_video_predict):
    #[x0,x1,x2,x3..xn]
    #[y0,y1,y2,y3,..ym]
    #print("!!!!!!!eiou_video!!!!!!!!")
    all_predicts = []
    all_groundtruths = []
    total_length = in_video_groundtruth[-1] - in_video_groundtruth[0]

   #read the input to all_groundtruths and all_predicts
    last_timestamp = -1
    last_predict_stamp = -1
    for time_stamp in in_video_groundtruth:        
        if(last_timestamp != -1):
            segment = [last_timestamp,time_stamp]
            all_groundtruths.append(segment)
        last_timestamp = time_stamp
    for predict_stamp in in_video_predict:
        if(last_predict_stamp != -1):
            predict_segment = [last_predict_stamp,predict_stamp]
            all_predicts.append(predict_segment)
        last_predict_stamp = predict_stamp

    #sorted by the second
    all_groundtruths.sort()
    all_groundtruths_sorted = all_groundtruths.copy()
    all_predicts.sort()
    all_predicts_sorted = all_predicts.copy()

    #store the segment length to the groundtruth_length
    groundtruth_length = []
    for groundtruth in all_groundtruths_sorted:  
        effect_segment_weight = groundtruth[1] - groundtruth[0]
        groundtruth_length.append(effect_segment_weight)
    
    #calcuate iou for each predict
    #1st loop for each predict, each predict can only have 1 ground truth id
    predict_gorundtruth = {}
    predict_id = 0
    for predict in all_predicts_sorted:
        predict_gorundtruth[predict_id] = (-1,0,0,0)
        groundtruth_id = 0
        max_weighted_iou = 0
        max_iou = 0
        for groundtruth in all_groundtruths_sorted:
             minov = minov_calucate(groundtruth,predict)
             maxov = maxov_calucate(groundtruth,predict)
             delta = 0
             if(minov > 0):
                 iou_current_predict = (minov + delta) / maxov

                 if(max_iou < iou_current_predict):
                     max_iou = iou_current_predict
                     predict_gorundtruth[predict_id] = (groundtruth_id,max_iou,groundtruth_length[groundtruth_id],minov)
             groundtruth_id = groundtruth_id + 1
        predict_id = predict_id + 1

    groundtruth_predicts = {} 
    #each groundtruth, key is groundtruth_id , value is the list of all its predits (predict_id,iou,weight,minov)
    for key, value in predict_gorundtruth.items():
            #print("predict_gorundtruth ",key,str(value))
            groundtruth_id,iou,weight,minov = value
            predict_id = key
            if(groundtruth_id not in groundtruth_predicts):
                groundtruth_predicts[groundtruth_id] = []
                groundtruth_predicts[groundtruth_id].append((predict_id,iou,weight,minov))
            else:
                groundtruth_predicts[groundtruth_id].append((predict_id,iou,weight,minov))

    #add penalty for multi wrong segments for one predict
    #2nd loop for each ground truth select the max miou as miou for the effect iou
    delta_wrong=0
    #missing part
    groundtruth_id=0
    
    #print(groundtruth_predicts)
    for i in range(len(all_groundtruths_sorted)):
        if((groundtruth_id not in groundtruth_predicts)):
            delta_wrong=delta_wrong+1
        groundtruth_id=groundtruth_id+1

    predict_ious = {} # this is the effect ious
    for key, value in groundtruth_predicts.items():
            groundtruth_id = key
            max_iou_id = -1
            max_iou = 0
            id = 0
            for items in value:
                predict_id,iou,weight,minov = items
                if(max_iou < iou):
                    max_iou_id = id
                    max_iou = iou
                id = id + 1

            id = 0
            has_multi_segs=0
            for items in value:
                predict_id,iou,weight,minov = items
                if(id != max_iou_id):
                    predict_ious[predict_id] = (-1,0,weight,minov)
                    has_multi_segs=has_multi_segs+1
                else:
                    predict_ious[predict_id] = (groundtruth_id,iou,weight,minov)
                id = id + 1
            #punish when  multi-segments
                delta_wrong=delta_wrong+has_multi_segs

    iou_sum = 0
    #print("predict_ious, ",predict_ious)
    for key, value in predict_ious.items():
            groundtruth_id,iou,weight,minov = value
            
            #print("iou,weight ",iou,weight)
            iou_sum = iou_sum + iou * weight

# test part
    weighted_total = sum([length for length in groundtruth_length])
    miou = iou_sum / weighted_total
    penalty=len(groundtruth_length)/(len(groundtruth_length)+delta_wrong)
    eiou=miou*penalty
    print("penalty predicts cnt is, ",delta_wrong)
    print("final eiou is, ",eiou)
    return eiou


def run_miou_v3_linear(test_data, ground_truth):
    id = 1
    
    results=[]
    for predict_data in test_data:
        print("!!!!!!!!!!!!!miou_v3_linear!!!!!!!!!!!!!!!!")
        video_sov_value = miou_v3_linear(ground_truth,predict_data)
        print("THE ", str(id),"results: ",str(predict_data), "its EIOU value is ", str(round(video_sov_value, 3)))
        id = id + 1
        results.append(str(round(video_sov_value, 3)))

    print(" ".join(results))

def Read_Seconds(rows):
    all_seconds=[]
    all_seconds.append(0)
    last_second=-1
    for row in rows:
        url,stepid,start_second,end_second=row.strip('\n').split('\t')
        all_seconds.append(int(start_second))
        last_second=end_second
    all_seconds.append(int(last_second))
    #print("all_seconds",all_seconds)
    return all_seconds

def run_by_file(in_test_file, in_predict_file,out_eiou_file,out_final_iou):
    testset={}
    predictset={}
    eiou_dic={}

    with open(in_test_file, 'r', encoding='utf-8') as f:
        last_url=""
        for line in f:

            url,stepid,start_second,end_second=line.strip('\n').split('\t')  
            if(last_url!=url):
                testset[url]=[]
                testset[url].append(line)
            else:
                testset[url].append(line)
            last_url=url

    with open(in_predict_file, 'r', encoding='utf-8') as f:
        for line in f:
            url,stepid,start_second,end_second=line.strip('\n').split('\t')    
            if(last_url!=url):
                predictset[url]=[]
                predictset[url].append(line)
            else:
                predictset[url].append(line)
            last_url=url

    eiou_avg=0.0
    
    with open(out_eiou_file,'w', encoding='utf-8') as f_write:
        for key, value in testset.items():
            if(key not in predictset):
                eiou_dic[key]=0
            else:
                predict=Read_Seconds(predictset[key])
                groundtruth=Read_Seconds(value)
                #print("groundtruth",groundtruth)
                #print("predict",predict)
                print(key)
                eiou=miou_v3_linear_clean(groundtruth,predict)
                eiou_avg=eiou_avg+eiou
            f_write.write(key+"\t"+str(eiou)+"\n")
    with open(out_final_iou,'w', encoding='utf-8') as f_write:
        eiou_avg=eiou_avg/len(testset)
        print("!!!!!!!!!final eiou is !!!!!!!!!", eiou_avg)
        f_write.write(str(eiou_avg)+"\n")


args = parser.parse_args()
print(args)
predit_dir=args.prediction_dir

for root,dirs,files in os.walk(predit_dir):   
    for file in files:
        if(file.endswith('.prediction')):
            path=predit_dir + "\\" + file
            eiou_details_file=predit_dir + "\\" + file[:-11]+".eiou.details.txt"
            eiou_final_file=predit_dir + "\\" + file[:-11]+".eiou.final.txt"
            run_by_file(args.ground_truth_file, path, eiou_details_file,eiou_final_file)

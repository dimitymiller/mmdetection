_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn_vocSplitLogits.py',
    '../_base_/datasets/voc0712Split.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
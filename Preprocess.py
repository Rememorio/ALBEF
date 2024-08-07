import json
import os

def create_json(image_dir, annotation_file, output_file):
    with open(annotation_file, 'r') as f:
        annotations = json.load(f)

    cc3m_data = []

    for annotation in annotations['annotations']:
        image_id = annotation['image_id']
        caption = annotation['caption']
        image_filename = f"{image_dir}/{image_id:012d}.jpg"
        cc3m_data.append({'image_id': image_id, 'image': image_filename, 'caption': caption})

    with open(output_file, 'w') as json_file:
        json.dump(cc3m_data, json_file)

# create coco_train.json
create_json('/home/data/ljf/workspace/SegmentationDataset/MSCOCO/train2017',
                 '/home/data/ljf/workspace/SegmentationDataset/MSCOCO/annotations/captions_train2017.json',
                 'data/coco_train2017.json')

# create coco_val.json
create_json('/home/data/ljf/workspace/SegmentationDataset/MSCOCO/val2017',
                 '/home/data/ljf/workspace/SegmentationDataset/MSCOCO/annotations/captions_val2017.json',
                 'data/coco_val2017.json')

# create coco_test.json
create_json('/home/data/ljf/workspace/SegmentationDataset/MSCOCO/test2017',
                 '/home/data/ljf/workspace/SegmentationDataset/MSCOCO/annotations/captions_val2017.json',
                 'data/coco_test2017.json')

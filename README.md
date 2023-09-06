

# 训练
python train.py --weights weights/yolov5n-seg.pt --cfg models/yolov5n-seg.yaml
    --data data/custom.yaml --hyp data/hyps/hyp.scratch-low.yaml \
    --epochs 100 --batch-size 8 --device 0 --workers 4 --name shape_yolov5n

# 验证
python val.py --weights runs/train-seg/shape_yolov5n/weights/best.pt --data data/custom.yaml --batch-size 16 --device 0 --name shape_yolov5n

# 测试
python predict.py --weights runs/train-seg/shape_yolov5n/weights/best.pt --source dataset/custom_dataset/images/test --data data/custom.yaml \
    --device 0 --name shape_yolov5n


# 预训练模型
https://github.com/ultralytics/yolov5/releases/tag/v7.0
去作者官网下载，下载后在主目录上新建一个weights的文件，全部放入即可。


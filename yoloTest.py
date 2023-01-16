def basic_setting():
    import os
    os.system("sed -i 's/OPENCV=0/OPENCV=1/' Makefile")
    os.system("sed -i 's/GPU=0/GPU=1/' Makefile")
    os.system("sed -i 's/CUDNN=0/CUDNN=1/' Makefile")
    os.system("sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile")
    os.system("sed -i 's/LIBSO=0/LIBSO=1' Makefile")
    os.system("make")
    os.system("chmod +x ./darknet")
    # !sed -i 's/OPENCV=0/OPENCV=1/' Makefile
    # !sed -i 's/GPU=0/GPU=1/' Makefile
    # !sed -i 's/CUDNN=0/CUDNN=1/' Makefile
    # !sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile
    # !sed -i 's/LIBSO=0/LIBSO=1' Makefile

    # !make
    # !chmod +x ./darknet

    # !sudo apt install dos2unix

    # !dos2unix ./data/list/train.txt
    # !dos2unix ./data/list/valid.txt
    # !dos2unix ./data/list/test.txt
    # !dos2unix ./data/ClassNames.names
    # !dos2unix ./data/maskDatas.data
    # !dos2unix ./cfg/yolov4-tiny-custom.cfg


def test_image():
    basic_setting()
    import os
    os.system("time ./darknet detector test data/maskDatas.data cfg/yolov4-tiny-custom.cfg backup/yolov4-tiny-custom_final.weights -ext_output -dont_show -save_labels -out output.json data/images/test.jpg")


def test_return_result():
    test_image()

    import json
    with open("output.json", "r") as file:
        result = json.load(file)[0]
    file.close()
    
    if len(result["objects"]) == 0:
        print("You can park here")
        return 1

    else:
        print("You cannot park here")
        return 0


test_return_result()
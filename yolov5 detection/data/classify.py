import  os
import shutil
import time
import pathlib
#将图片和标签分别放入不同的文件夹
def classify():
    train_file_names = os.listdir('./train')
    val_file_names = os.listdir('./val')
    # print(train_file_names[0].split('.')[1])
    st_time = time.time()
    print("开始train文件夹转移操作~")
    for file in train_file_names:
        try:
            if file.split('.')[1] == 'jpg':
                shutil.move('./train/{}'.format(file),'./train/images')
            elif file.split('.')[1] == 'txt':
                shutil.move('./train/{}'.format(file),'./train/labels')
        except:
            print(file+"文件转移出错")
            continue
    end_time = time.time()
    print("耗时：%d"%(end_time-st_time))
    print("=============================================================")
    print("开始val文件夹的操作")
    st_time = time.time()
    for file in val_file_names:
        try:
            if file.split('.')[1] == 'jpg':
                shutil.move('./val/{}'.format(file),'./val/images')
            elif file.split('.')[1] == 'txt':
                shutil.move('./val/{}'.format(file),'./val/labels')
        except:
            print(file + "文件转移出错")
            continue
    end_time = time.time()
    print("耗时：%d" % (end_time - st_time))
    print("转移成功~")

def delete_file():#删除没有标签的图片
    labels_files = os.listdir('./train/labels')
    images_files = os.listdir('./train/images')
    for file in images_files:
        name = file.split('.')[0]+".txt"
        if name not in labels_files:
            print(file+"没有标签值，已删除~")
            os.remove('./train/images/{}'.format(file))
    print("完工~")

if __name__ == '__main__':
    # classify()
    delete_file()
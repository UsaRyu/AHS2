import glob
import cv2
import pathlib

torv = ['train/','validation/']
signs = ['corna','peace','shaka_hang','thumbs_up']

for j in range(len(torv)):
    for k in range(len(signs)):

        #画像の処理
        input_dir = './original_hand_data/' + torv[j] + signs[k]
        # 保存するファルダ
        output_dir = './processed_hand_data/' + torv[j] + signs[k]

        # フォルダ内に保存されているファイル一覧
        image_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))
        #print(image_list)

        for i in range(len(image_list)):
            # 画像一枚を読み込み
            img = cv2.imread(str(image_list[i]))
            # トリミング
            img_tri_true = img[100 : 1100, 500 : 1400]
            # 保存先
            output_path = output_dir + '/' + image_list[i].name
            # 画像保存 
            cv2.imwrite(output_path, img_tri_true)

#画像の処理
input_dir = './testdata/'
# 保存するファルダ
output_dir = './testdata/'

# フォルダ内に保存されているファイル一覧
image_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))
#print(image_list)

for i in range(len(image_list)):
    # 画像一枚を読み込み
    img = cv2.imread(str(image_list[i]))
    # トリミング
    img_tri_true = img[100 : 1100, 500 : 1400]
    # 保存先
    output_path = output_dir + '/' + image_list[i].name
    # 画像保存 
    cv2.imwrite(output_path, img_tri_true)

'''
for j in range(len(torv)):
    for k in range(len(signs)):
        #画像の処理
        input_dir = './original_hand_data/' + torv[j] + signs[k]
        # 保存するファルダ
        output_dir = './processed_hand_data/' + torv[j] + signs[k]

        # フォルダ内に保存されているファイル一覧
        image_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))
        print(image_list)

        for i in range(len(image_list)):
            # 画像一枚を読み込み
            img = cv2.imread(str(image_list[i]))
            # トリミング
            #img_tri_true = img[100 : 1100, 500 : 1400]
            # 保存先
            output_path = output_dir + '/' + image_list[i].name
            # 画像保存 
            cv2.imwrite(output_path, img)
'''
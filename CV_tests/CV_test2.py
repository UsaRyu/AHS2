#import matplotlib.pyplot as plt
import glob
import cv2
import pathlib
"""
img = cv2.imread('test_corna.jpg')
img_gray = cv2.imread('test_corna.jpg', 0)
cv2.imwrite('test_corna_copy.jpg', img)
cv2.imwrite('test_corna_gray.jpg', img_gray)

print(img.shape)

#plt.imshow(img)

img_tri1 = img[0 : 50, 0: 50]
cv2.imwrite('test_corna_tri1.jpg', img_tri1)
img_tri2 = img[50 : 150, 100 : 250]
cv2.imwrite('test_corna_tri2.jpg', img_tri2)

img_tri_true = img[100 : 1100, 500 : 1400]
cv2.imwrite('test_corna_tri_true.jpg', img_tri_true)

for i in range(0,2):
    img = cv2.imread('test/test_corna'+str(i)+'.jpg')
    img_tri_true = img[100 : 1100, 500 : 1400]
    cv2.imwrite('test_corna_tri_true.jpg', img_tri_true)
    cv2.imwrite('test_corna_tri_true{0}.jpg'.format(i), img_tri_true)
    #cv2.imwrite('test_corna_tri_true'+str(i)'.jpg', img_tri_true)
"""
input_dir = './testbox/test'
# 保存するファルダ
output_dir = './testbox/test2'

# フォルダ内に保存されているファイル一覧
image_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))

for i in range(len(image_list)):
    # 画像一枚をグレースケールで読み込み
    img = cv2.imread(str(image_list[i]))
    # (100,100)にリサイズ
    img_tri_true = img[100 : 1100, 500 : 1400]
    # 保存先
    output_path = output_dir + '/' + image_list[i].name
    # 画像保存 
    cv2.imwrite(output_path, img_tri_true)





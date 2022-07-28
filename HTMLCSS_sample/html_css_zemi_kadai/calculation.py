def trapezoid_area(top, bottom, height):
    try:
        top, bottom, height = int(top), int(bottom), int(height) #整数以外の入力を受け付けない
        if top <= 0 or bottom <= 0 or height <= 0: #長さ0、負の値は図形的にありえないので弾く
            raise Exception #例外に飛ばす
        area = (top + bottom)*height*0.5
        return area
    except:
        return '自然数を入力してください'

# if __name__ == '__main__':
#     top, bottom, height = input().split()
#     print(trapezoid_area(top, bottom, height))
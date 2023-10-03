# 奇数で逆三角形に配置
import numpy as np
from PIL import Image
import matplotlib.pyplot  as plt
import glob

# 画像のディレクトリ
dir = './img'
# コマ送りに使う画像ファイル
file_list = glob.glob(dir + '/*')

fig = plt.figure(figsize=(5, 3), dpi=350)
grid = plt.GridSpec(2, 6)  # グリッド設定　2行4列

# 画像を並べる
for i, file in enumerate(file_list):
    img = Image.open(file)  # 画像を開く

    # 位置とタイトル 3段1列
    if 0 <= i and i < 3:
        num = i * 2
        # 0行目, numからnum+2列目を使う
        # 0:2 2:4 4:6
        fig.add_subplot(grid[0, num:num+2])
    else:
        num = (i - 3) * 2 + 1
        # 1行目, numからnum+2列目を使う
        # 1:3 3:5
        fig.add_subplot(grid[1, num:num+2])

    
    # 線を消す
    lines = ['right', 'top', 'bottom', 'left']
    for line in lines:
        plt.gca().spines[line].set_visible(False)

    # ラベルと補助線を消す
    plt.tick_params(labelbottom=False, 
                    labelleft=False, 
                    labelright=False, 
                    labeltop=False,
                    bottom=False, 
                    left=False, 
                    right=False, 
                    top=False)
    plt.imshow(img)

# 出力画像を保存
plt.savefig('./result/odd.jpg')
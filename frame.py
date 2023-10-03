import numpy as np
from PIL import Image
import matplotlib.pyplot  as plt
from natsort import natsorted
import glob

# 画像のディレクトリ
dir = './cat_frames_img'
# コマ送りに使う画像ファイル名をソート
file_list = natsorted(glob.glob(dir + '/*'))

# 画像を並べる
fig = plt.figure(figsize=(6, 3), dpi=350)
for i, file in enumerate(file_list):
    img = Image.open(file)  # 画像を開く
    
    # 3段8列
    fig.add_subplot(3, 8, i+1)
    
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
plt.savefig('./result/frames.jpg')
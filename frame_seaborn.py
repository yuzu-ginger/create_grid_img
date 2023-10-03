# seaborn で作る
import matplotlib.pyplot as plt
import seaborn_image as isns
from natsort import natsorted
import numpy as np
from PIL import Image
import glob

# 画像のディレクトリ
dir = './cat_frames_img'
# コマ送りに使う画像ファイル名をソート
file_list = natsorted(glob.glob(dir + '/*'))

# set context
isns.set_context("talk") #or notebook
plt.rcParams['figure.dpi'] = 350

# set global image settings
isns.set_image(cmap="afmhot",origin="upper")

# 画像を並べる
fig = plt.figure(figsize=(6, 3), dpi=350)
for i, file in enumerate(file_list):
    img = Image.open(file)  # 画像を開く

    # 3行8列
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
    plt.tight_layout()
    plt.imshow(img)


# 出力画像を保存
plt.savefig('./result/frames_seaborn.jpg')
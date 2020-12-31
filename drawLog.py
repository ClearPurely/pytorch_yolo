
import glob
import numpy as np
import matplotlib.pyplot as plt
#import os; os.system('rm -rf results.txt && wget https://storage.googleapis.com/ultralytics/results_v1_0.txt')

s = ['GIoU', 'Objectness', 'Classification', 'Precision', 'Recall',
     'val GIoU', 'val Objectness', 'val Classification', 'mAP@0.5', 'F1']
#glob返回所有匹配的文件路径列表。

#连续绘图
def plot_all():
    plt.figure(figsize=(16, 8))
    files = sorted(glob.glob('backups/results.txt'))
    for f in files:
        results = np.loadtxt(f, usecols=[2, 3, 4, 8, 9, 12, 13, 14, 10, 11]).T
        n = results.shape[1]
        for i in range(10):
            plt.subplot(2, 5, i + 1)
            plt.plot(range(1, n), results[i, 1:], marker='.', label=f)
            plt.title(s[i])
            if i == 0:
                plt.legend()
    plt.show()

#单个绘图
def plot_one():
    file = 'backups/results.txt'
    results = np.loadtxt(file, usecols=10).T  # column 16 is mAP
    n = results.__len__()
    plt.plot(range(1, n),results[1:], marker='.', label=file)
    plt.title('mAP@0.5')
    plt.show()
    # plt.savefig('plot/plot.png')


if __name__ == "__main__":
    plot_all()
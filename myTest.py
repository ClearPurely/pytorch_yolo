from models import *
import torch
from numpy import *

def test1():
    convert('cfg/yolov3.cfg', 'weights/yolov3.weights')

def test2():
    print(torch.__version__)  # 查看pytorch版本
    print(torch.cuda.is_available())  # 判断pytorch是否支持GPU加速
    print(torch.version.cuda)  # 查看CUDA版本
    print(torch.backends.cudnn.version())  # 查看cuDNN版本
    print(torch.cuda.get_device_name(0))  # 查看显卡类型

def test3():
    L = [[1,0,0,0],[ -2,1,0,0],[ 3,1 ,1,0],[-1  , -3  ,   3 ,    1]]
    U = [[2 , 3 , 4 , 5],[ 0, 1 , 0 , 1],[0  , 0   , 2    -3],[0 , 0  , 0 ,  5]]
    jL = mat(L)
    jU = mat(U)
    a = jL * jU
    print(a)

def test4():
    import torch
    x = torch.rand(5, 3)
    print(x)

def test5():
    from utils import utils
    utils.plot_results()


if __name__ == '__main__':
    test5()
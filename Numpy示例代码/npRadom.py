import numpy as np

# 生成范围随机数
x_data = np.random.uniform(-1.0, 1.0, 10)
print(x_data)

# 生成正态分布随机数,期望值10，标准差2，个数10
x_data = np.random.normal(10, 2, 10)
print(x_data)

# 生成标准正太分布随机数，期望值为0，标准差为1
x_data = np.random.randn(2, 2)
print(x_data)

# 生成[0, 1)之间2x2随机数矩阵
x_data = np.random.rand(2, 2)
print(x_data)

# 生成[5, 10)之间10个随机数，类型为int
x_data = np.random.randint(5, 10, 10, 'int')
print(x_data)

# 在[0,1）内产生随机数
x_data = np.random.random([3, 3])
print(x_data)

# 从给定的数据集合中随机选取3个数
x_data = np.random.choice([1, 3, 5, 7, 9], 3)
print(x_data)

#生成从1-10的等差数列，个数为20
x_data = np.linspace(1, 10, 20)
print(x_data)

import os
import psutil

# if (os.system("ping -c 2 baidu.com") != 0):
#     print("No internet")
#     exit(1)


"""获取所有挂载点信息"""
partitions = psutil.disk_partitions()

print("设备名称\t挂载点\t文件系统类型")
print("-" * 50)

for partition in partitions:
    print(f"{partition.device}\t{partition.mountpoint}\t{partition.fstype}")



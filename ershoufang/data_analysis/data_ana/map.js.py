import matplotlib.pyplot as plt
import pandas as pd

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

"""1、数据加载"""
# 定义加载数据的文件名
filename = "../data_file/ershoufang-clean-utf8.csv"
# 自定义数据的行列索引（行索引使用pd默认的，列索引使用自定义的）
names = [
        "id","communityName","areaName","total","unitPriceValue",
        "fwhx","szlc","jzmj","hxjg","tnmj",
        "jzlx","fwcx","jzjg","zxqk","thbl",
        "pbdt","cqnx","gpsj","jyqs","scjy",
        "fwyt","fwnx","cqss","dyxx","fbbj",
        ]
# 自定义需要处理的缺失值标记列表
miss_value = ["null","暂无数据"]
# 数据类型会自动转换
# 使用自定义的列名，跳过文件中的头行，处理缺失值列表标记的缺失值
df = pd.read_csv(filename,skiprows=[0],names=names,na_values=miss_value)

"""3、合并数据，并按格式输出数据"""
# 合并数据
df_latlng = pd.read_csv("../data_file/latlng.csv",skiprows=[0],names=["did","id","communityName","lat","lng"])
del df_latlng["did"]
del df_latlng["communityName"]
df_merge = pd.merge(df,df_latlng,on="id")

# 小于200万
# xiaoyu = df_merge[df_merge["total"]]
# xiaoyu2 = df_merge.loc[df_merge["total"]<201]


"""4、生成需要的格式文件"""
# unitprice = "../data_ana/map/unitprice.js"
# with open(unitprice,"w") as file_out:
#     for lng,lat,price in zip(list(df_merge["lng"]),list(df_merge["lat"]),list(df_merge["unitPriceValue"])):
#         # out = str(lng)+","+str(lat)
#         out = '{\"lng\":'+str(lng)+',\"lat\":'+str(lat)+',\"count\":'+str(price)+'},'
#         file_out.write(out)
#         file_out.write("\n")
total = "../data_ana/map/total.js"
with open(total,"w") as file_out:
    for lng,lat,price in zip(list(df_merge["lng"]),list(df_merge["lat"]),list(df_merge["total"])):
        # out = str(lng)+","+str(lat)
        out = '{\"lng\":'+str(lng)+',\"lat\":'+str(lat)+',\"count\":'+str(price)+'},'
        file_out.write(out)
        file_out.write("\n")

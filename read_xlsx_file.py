import numpy as np
import pandas as pd
import os

def _init_humidity():
    beta = pd.read_excel(io="数据集/基本数据/附件3、土壤湿度2022—2012年.xls")
    beta = beta.sort_values(by=['年份', '月份'], ascending=[False, False]).iloc[::-1]
    # beta.to_excel('beta.xls')
    # print(self.beta.columns)
    return beta

def _init_graze():
    graze_indensity = pd.read_excel(io='数据集/监测点数据/附件14：内蒙古自治区锡林郭勒盟典型草原不同放牧强度土壤碳氮监测数据集（2012年8月15日-2020年8月15日）/内蒙古自治区锡林郭勒盟典型草原不同放牧强度土壤碳氮监测数据集（2012年8月15日-2020年8月15日）.xlsx')
    # print(graze_indensity.columns)
    return graze_indensity

def _init_surface_emission():
    surface_emission = pd.read_excel(io='数据集/基本数据/附件4、土壤蒸发量2012—2022年.xls')
    surface_emission= surface_emission.sort_values(by=['年份', '月份'], ascending=[False, False]).iloc[::-1]
    # print(surface_emission.columns)
    return surface_emission


def _init_climate():
    file_path = "数据集/基本数据/附件8、锡林郭勒盟气候2012-2022"
    file_ls = [os.path.join(file_path,  file_name) for file_name in   os.listdir(file_path)]
    climate  = pd.read_excel(io = file_ls[0])
    for i,value in enumerate(file_ls):
        if i!=0:
            new_sheet = pd.read_excel(io = value)
            climate = pd.concat((climate, new_sheet))
    # climate.to_excel('climate.xls')
    # print(self.climate.columns)
    return climate

def _init_ndvi():
    ndvi = pd.read_excel(io='数据集/基本数据/附件6、植被指数-NDVI2012-2022年.xls')
    ndvi= ndvi.sort_values(by=['年份', '月份'], ascending=[False, False]).iloc[::-1]
    return ndvi

def _init_runoff():
    runoff = pd.read_excel('数据集/基本数据/附件9、径流量2012-2022年.xlsx')
    runoff= runoff.sort_values(by=['年份', '月份'], ascending=[False, False]).iloc[::-1]
    return runoff

def _init_block_plant():
    """
    ['年份', '轮次', '处理', '日期', '植物种名', '植物群落功能群', '放牧小区Block', '重复', '营养苗',
   '生殖苗', '株/丛数', '丛幅1', '丛幅2', '鲜重(g)', '干重(g)', '平均每珠干重']
    :return:
    """
    plant = pd.read_excel('数据集/监测点数据/附件15：内蒙古自治区锡林郭勒盟典型草原轮牧放牧样地群落结构监测数据集（2016年6月-2020年9月）。/内蒙古自治区锡林郭勒盟典型草原轮牧放牧样地群落结构监测数据集（201.xlsx',sheet_name='2016-2020物种数据库')
    plant = plant.sort_values(by=['日期'], ascending=[False]).iloc[::-1]
    return plant



def calculate_icmax():
    LAI = pd.read_excel('数据集/基本数据/附件10、叶面积指数（LAI）2012-2022年.xls')
    LAI= LAI.sort_values(by=['年份', '月份'], ascending=[False, False]).iloc[::-1]
    LAIL = LAI['低层植被(LAIL,m2/m2)'][:123]   # 到202203截至
    LAIL = np.array(LAIL)
    icmax = 0.935+0.498*LAIL-0.00575*LAIL**2
    """
    ICstore,草地的植被直接决定放牧的强度，而植被的截流量能最好反映植被的生长能力，
    依照递推关系，放牧强度与植被的截流量存在正相关关系
    """
    Rcum = _init_climate().climate['降水量(mm)']
    return icmax

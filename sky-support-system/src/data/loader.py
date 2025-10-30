import pandas as pd

def load_meterological_data(file_path):
    """
    加载气象数据文件
    参数:
        file_path (str):数据文件的路径 (支持.csv或..xlsx)
    返回:
        pandas.DataFrame:加载后的数据框
    """
    #通过文件后缀判断格式
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("不支持的文件格式!请提供.csv或.xlsx文件。")
    
    #打印数据基本信息，确认加载成功
    print(f"数据加载成功！数据集形状：{df.shape}")
    print("数据前5行:")
    print(df.head())


    return df

#测试代码：当直接运行这个文件时执行
if __name__ == "__main__":
    #在这里替换成你实际的气象数据文件路径
    test_file = "你的气象数据文件。cvs"  #示例："./data/raw_weather.csv"
    data = load_meterological_data(test_file)
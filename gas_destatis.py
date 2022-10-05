import pandas as pd

DATA_URL = 'https://www.destatis.de/DE/Themen/Wirtschaft/Konjunkturindikatoren/Preismonitor/_Grafik/_Interaktiv/energie-wasser.html?cms_showChartData=1'

def get_data():
  dfs = pd.read_html(DATA_URL)
  gas_df = dfs[0]
  return gas_df
  
if __name__ == "__main__":
  new_data = get_data()
  new_data.to_csv('energie_wasser.csv')

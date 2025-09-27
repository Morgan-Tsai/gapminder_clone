import sqlite3
import pandas as pd
import plotly.express as px

#連線資料庫
connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting;""",con=connection)
connection.close()
#print(plotting_df.shape)

#繪製成品動畫
fig = px.scatter(plotting_df,x="gdp_per_capita",y="life_expectancy",
                 animation_frame="dt_year" ,animation_group="country_name", #animation_frame:時間軸依據
                 size="population",color="continent",hover_name="country_name", #size:氣泡大小 hover_name:游標顯示
                 size_max=100,range_x=[500,100000],range_y=[20,90],log_x=True, #log_x:x軸的對數刻度，適用單尾分布
                 title="Gapminder Clone 1800-2023")
fig.write_html("gapminder_clone.html",auto_open=True)


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#資料庫連線
connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting;""",con=connection)
connection.close()
#print(plotting_df.shape)

#繪製動畫
fig,ax = plt.subplots()
def update_plot(year_to_plot:int):
    ax.clear() #清空畫布
    subset_df = plotting_df[plotting_df["dt_year"] == year_to_plot] #篩選特定年份資料
    lex = subset_df["life_expectancy"].values #y軸
    gdp_pcap = subset_df["gdp_per_capita"].values #x軸
    cont = subset_df["continent"].values #顏色依據
    #print(subset_df["continent"].unique())
    color_map = {
        "asia":"r",
        "africa":"g",
        "europe":"b",
        "americas":"c" #cyan
    }

    for xi,yi,ci in zip(gdp_pcap,lex,cont):
        ax.scatter(xi,yi,color=color_map[ci])
    ax.set_title(f"The world in {year_to_plot}")
    ax.set_xlabel("GDP Per Capita(in USD)")
    ax.set_ylabel("Life Expectancy")
    ax.set_xlim(0,100000)
    ax.set_ylim(20,100)
    plt.show()

ani = animation.FuncAnimation(fig,func=update_plot,frames=range(2000,2024),interval=10) 
#frames:定義動畫的幀數 #interval:每幀之間的時間間隔（毫秒）
ani.save("animation.gif",fps=10) #fps:每秒顯示幀數，控制動畫播放速度

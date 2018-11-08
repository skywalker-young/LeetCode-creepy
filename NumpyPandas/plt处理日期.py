
#画图做k线
def plot_k_series(df):
    num_of_ticks=len(df)
    fig,ax=plt.subplots(figsize=(20,10))
    fig.subplots_adjust(bottom=0.2)
    dates=df['tradeDate']
    #打印日期
    ax.set_xticks(np.linspace(1,num_of_ticks,num_of_ticks))
    ax.set_xticklabels(list(dates))
    mpf.candlestick2_ohlc(ax,list(df.openPrice),list(df.highestPrice),list(df.lowestPrice),\
                          list(df.closePrice),width=0.6,colorup='r',colordown='g',alpha=0.7)
    plt.grid(True)
    plt.setp(plt.gca().get_xticklabels(),rotation=30)
    return ax

def plot_lines(ax, fx_plot, fx_offset):
    # 绘制笔和线段
    # ax 绘图区域
    # fx_plot
    plt.plot(fx_offset, fx_plot, 'k', lw=1)
    plt.plot(fx_offset, fx_plot, 'o')
    

def plot_pivot(ax, date_interval, price_interval):
    #
    # 绘制中枢
    start_point = (date_interval[0], price_interval[0])
    width = date_interval[1] - date_interval[0]
    height =  price_interval[1] - price_interval[0]
    ax.add_patch(patches.Rectangle(start_point,width, height,linewidth=2,edgecolor='g',facecolor='none'))
    return

'''
This module has utilities1 for the arithmetic functions.
The parameters are of variable length.
'''

__author__ = 'vinay'
__version__ = "alpha_1"


def myvsum(*args):
    '''
    function which takes in variable count of numbers
    and returns their sum
    '''
    s = 0
    for n in args:
        s = s + n
    return s     
    
def myvproduct(*args):
    '''
    function which takes in variable count of numbers
    and returns their product
    '''
    p = 1
    for n in args:
        p = p * n
    return p

#bbox [left,bottom,width,height]
def draw_table(axes,ct, tc='red',zo=14,left=0.06,bottom=0.06,fs=18):
    import numpy as np
    #import matplotlib.pyplot as plt
    #stats_table = table(ax=axes, cellText=ct,bbox =[left,bottom, 2,1.3],
    #                                             cellLoc ='left',alpha=0.4,zorder=zo,edges ='closed')
    
    axes.set_axis_off() 
    stats_table = axes.table(cellText = ct,cellLoc ='left',
                             bbox =[left,bottom, 0.7,0.9],zorder=zo)         


    for cell in stats_table._cells:
        stats_table._cells[cell].set_alpha(0.1)    
    for key, cell in stats_table.get_celld().items():
        cell.set_linewidth(1)
        cell.set_edgecolor("w")
        cell.set_facecolor("white")
        cell.get_text().set_fontsize(fs)
        cell.get_text().set_color(tc)
    axes.grid()
    
def draw3d(n3d):
    import numpy as np
    import matplotlib.pyplot as plt
    if n3d.ndim == 2:
        n3d = n3d.reshape(n3d.shape[0],n3d.shape[1],1)
    print(n3d.shape)
    plt.style.use('classic')

    text_color_list = list('rgbmc'*20)
    zolist = list(range(28,7,-1))
    #zolist = [24]*8
    leftlist = np.arange(0,1,0.03)
    bottomlist = np.arange(0,1,0.03)
    
    fig, ax = plt.subplots(figsize=(9,6))
    
    
    for d in range(n3d.shape[-1]):
        draw_table(ax,n3d[:,:,d],tc=text_color_list[d],zo=zolist[d],
                   left=leftlist[d],bottom=bottomlist[d],fs=18-d*1)

    plt.text(0,1,str(n3d.shape))
    plt.axis('off') 
    plt.tight_layout()
    plt.show()    
 

if __name__  == '__main__':
    s = myvsum(1,2,3,4,5,6,7)
    print(s)
    p = myvproduct(1,2,3,4,5,6,7)
    print(p)
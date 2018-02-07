import matplotlib.pyplot as plt
def graph_adder(title):      # graph_no denotes the graph number used as a iterator in PDFgenerator
    f=open('test2.txt')
    fig=plt.figure()
    n=int(f.readline())
    ax=plt.gca()
    ax.set_facecolor((1,1,0.7))
    for i in range(n):
        a=list(map(float,f.readline().strip().split()))
        b=list(map(float,f.readline().strip().split()))
        plt.plot(a,b)
        for i in range(len(a)):
            plt.plot(a[i],b[i],'g*')
    plt.title(title)
    fig.savefig('C:/Users/Win 8.1/Desktop/GraphtoPdf xporter/temp/temp_%s.png'%title)
    plt.show()
    
    f.close()


#graph_adder(1)



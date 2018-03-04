import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as grd

# PDF package
from matplotlib.backends.backend_pdf import PdfPages


def data_loader():
    with open("Input.txt", 'r') as f:
        n = int(f.readline().strip())
        x_label = f.readline().strip().split()
        x = [list(map(int, f.readline().strip().split())) for i in range(n)]
        y_label = f.readline().strip().split()
        y = [list(map(int, f.readline().strip().split())) for i in range(n)]
    return n, x_label, x, y_label, y


with PdfPages("GraphtoPdf.pdf") as pdf:
    data = data_loader()
    for i in range(0, data[0], 2):
        #  A4 size in inches
        plt.figure(figsize=(8.27, 11.69))
        # gridspec object with grid parameters mxn
        gs = grd.GridSpec(2, 1)
        # Layout customization using top bottom left right parameters
        gs.update(top=0.98)
        plt.title("Page %d" % i)
        for j in range(2):
            if i+j>data[0]-1:
                break
            exec("ax = plt.subplot(gs[%d])"%j)
            plt.plot(data[2][i+j], data[4][i+j], color='r', linewidth=2.0)
            plt.xlabel("%s" % data[1][i+j])
            plt.ylabel("%s" % data[3][i+j])
            ax = plt.gca()
            ax.set_facecolor((1, 1, 0.7))
            # plt.title("%s" % title)

        pdf.savefig()



    d = pdf.infodict()
    d['Title'] = "GraphtoPdf"
    d["Author"] = "Ashutosh Naveen"
    d["Subject"] = "Converted graphs from tabulated data"
    d['Keywords'] = "PdfPages keywords author title subject"
    d["CreationDate"] = datetime.datetime(2018, 3, 4)
    d['ModDate'] = datetime.datetime.today()

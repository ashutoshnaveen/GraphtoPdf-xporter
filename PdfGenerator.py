import datetime
import numpy as np
import matplotlib.pyplot as plt

## PDF package
from matplotlib.backends.backend_pdf import PdfPages


with PdfPages("multipage_pdf.pdf") as pdf:
    plt.figure(figsize=(3,3))
    plt.plot(range(7),[3,1,4,1,5,9,2],'r-o')
    plt.title('page one')
    pdf.savefig()       # save the current fig to Pdf pages
    plt.close()

    plt.rc('text',usetex=False)
    fig1=plt.figure(figsize=(8,6))
    x=np.arange(0,5,0.1)
    plt.plot(x,np.sin(x),'b-')
    plt.title('Page Two')   
    pdf.attach_note("plot of sinx")

    pdf.savefig(fig1)
    plt.close()


    plt.rc('text',usetex=False)
    fig2=plt.figure(figsize=(4,5))
    plt.plot(x,x*x,'ko')
    plt.title("Page three")
    pdf.savefig(fig2)
    plt.close()

    d=pdf.infodict()
    d['Title']="Multipage Pdf"
    d["Author"]="Ashutosh"
    d["Subject"]="how to create a multipage pdf file with its metadata ausing matplotlib"
    d['Keywords']="PdfPages multipage keywords author title subject"
    d["CreationDate"]=datetime.datetime(2009,11,13)
    d['ModDate']=datetime.datetime.today()

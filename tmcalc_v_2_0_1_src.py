from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sys
import webbrowser
import math

proVer = '2.0.1'
rlsDate = '2022-02-14'

root = Tk()
root.title(f'Tm.Calc v{proVer}')

wideLogo = ImageTk.PhotoImage(Image.open('assets/tmcalc_main.png'))
Label(image = wideLogo).grid(row = 0, column = 0, columnspan = 5)

proInfoFrame = LabelFrame(root, borderwidth = 0, highlightthickness = 0)
proInfoFrame.grid(row = 1, column = 0, columnspan = 5, sticky = W + E)
Label(proInfoFrame, text = f'\nVer. {proVer} ({rlsDate})', font = ('Helvetica', 16, 'bold')).pack()
Label(proInfoFrame, text = 'A melting temperature calculator.\n').pack()

waveLength, decayTime = [], []
waveMatrix, timeMatrix = {}, {}

fName = StringVar()
fileName = ''


def calctm():
    global pEn1Val, pEn2Val, pEn3Val, pEn4Val, pEn5Val, pEn6Val
    global pEn1Seq, pEn2Seq, pEn3Seq, pEn4Seq, pEn5Seq, pEn6Seq
    global saltIni, primerIni
    global paraHS

    pEn1Seq = str(pEn1Val.get()).strip().upper()
    pEn2Seq = str(pEn2Val.get()).strip().upper()
    pEn3Seq = str(pEn3Val.get()).strip().upper()
    pEn4Seq = str(pEn4Val.get()).strip().upper()
    pEn5Seq = str(pEn5Val.get()).strip().upper()
    pEn6Seq = str(pEn6Val.get()).strip().upper()
    saltConc = saltIni.get()
    primerConc = primerIni.get()

    resWin = Toplevel()
    resWin.title('Results')

    if pEn1Seq:
        noA = 0
        noT = 0
        noC = 0
        noG = 0
        for i in pEn1Seq:
            if i == 'A':
                noA += 1
            elif i == 'T':
                noT += 1
            elif i == 'C':
                noC += 1
            elif i == 'G':
                noG += 1
        gcPer = (noC+noG)*100/(noA+noT+noC+noG)

        wallace = 2*noA+2*noT+4*noC+4*noG
        gcMethod = 81.5+16.6*math.log10(saltConc/1000)+41*gcPer/100-primerConc/(noA+noT+noC+noG)  

        sumH = 0
        sumS = 0
        neiPair = [pEn1Seq[j:j+2] for j in range(len(pEn1Seq)-1)]
        for k in neiPair:
            sumH += paraHS[k][0]
            sumS += paraHS[k][1]
        
        nnM = (1000*sumH/(-10.8+sumS+1.987*math.log(primerConc/4000000000)))-273.15+16.6*math.log10(saltConc/1000)

        pEn1Seq2 = StringVar()
        pEn1Seq2.set(pEn1Seq)

        Label(resWin, text = f'(1)  {pEn1Seq}', font = ('Helvetica', 15, 'bold')).grid(row = 1, column = 0, columnspan = 2)
        Label(resWin, text = f'GC = {round(gcPer, 1)}%, Length = {len(pEn1Seq)}').grid(row = 2, column = 0, columnspan = 2)
        Label(resWin, text = f'      Nearest Neighbor Method: ').grid(row = 3, column = 0)
        Label(resWin, text = f'               Wallace Method: ').grid(row = 4, column = 0)
        Label(resWin, text = f'                   GC% Method: \n').grid(row = 5, column = 0)
        Label(resWin, text = f' {round(nnM, 1)}').grid(row = 3, column = 1)
        Label(resWin, text = f' {round(float(wallace), 1)}').grid(row = 4, column = 1)
        Label(resWin, text = f' {round(gcMethod, 1)}\n').grid(row = 5, column = 1)

    if pEn2Seq:
        noA = 0
        noT = 0
        noC = 0
        noG = 0
        for i in pEn2Seq:
            if i == 'A':
                noA += 1
            elif i == 'T':
                noT += 1
            elif i == 'C':
                noC += 1
            elif i == 'G':
                noG += 1
        gcPer = (noC+noG)*100/(noA+noT+noC+noG)

        wallace = 2*noA+2*noT+4*noC+4*noG
        gcMethod = 81.5+16.6*math.log10(saltConc/1000)+41*gcPer/100-primerConc/(noA+noT+noC+noG)  

        sumH = 0
        sumS = 0
        neiPair = [pEn2Seq[j:j+2] for j in range(len(pEn2Seq)-1)]
        for k in neiPair:
            sumH += paraHS[k][0]
            sumS += paraHS[k][1]
        
        nnM = (1000*sumH/(-10.8+sumS+1.987*math.log(primerConc/4000000000)))-273.15+16.6*math.log10(saltConc/1000)

        pEn2Seq2 = StringVar()
        pEn2Seq2.set(pEn2Seq)

        Label(resWin, text = f'(2)  {pEn2Seq}', font = ('Helvetica', 15, 'bold')).grid(row = 6, column = 0, columnspan = 2)
        Label(resWin, text = f'GC = {round(gcPer, 1)}%, Length = {len(pEn2Seq)}').grid(row = 7, column = 0, columnspan = 2)
        Label(resWin, text = f'      Nearest Neighbor Method: ').grid(row = 8, column = 0)
        Label(resWin, text = f'               Wallace Method: ').grid(row = 9, column = 0)
        Label(resWin, text = f'                   GC% Method: \n').grid(row = 10, column = 0)
        Label(resWin, text = f' {round(nnM, 1)}').grid(row = 8, column = 1)
        Label(resWin, text = f' {round(float(wallace), 1)}').grid(row = 9, column = 1)
        Label(resWin, text = f' {round(gcMethod, 1)}\n').grid(row = 10, column = 1)

    if pEn3Seq:
        noA = 0
        noT = 0
        noC = 0
        noG = 0
        for i in pEn3Seq:
            if i == 'A':
                noA += 1
            elif i == 'T':
                noT += 1
            elif i == 'C':
                noC += 1
            elif i == 'G':
                noG += 1
        gcPer = (noC+noG)*100/(noA+noT+noC+noG)

        wallace = 2*noA+2*noT+4*noC+4*noG
        gcMethod = 81.5+16.6*math.log10(saltConc/1000)+41*gcPer/100-primerConc/(noA+noT+noC+noG)  

        sumH = 0
        sumS = 0
        neiPair = [pEn3Seq[j:j+2] for j in range(len(pEn3Seq)-1)]
        for k in neiPair:
            sumH += paraHS[k][0]
            sumS += paraHS[k][1]
        
        nnM = (1000*sumH/(-10.8+sumS+1.987*math.log(primerConc/4000000000)))-273.15+16.6*math.log10(saltConc/1000)

        pEn3Seq2 = StringVar()
        pEn3Seq2.set(pEn3Seq)

        Label(resWin, text = f'(3)  {pEn3Seq}', font = ('Helvetica', 15, 'bold')).grid(row = 11, column = 0, columnspan = 2)
        Label(resWin, text = f'GC = {round(gcPer, 1)}%, Length = {len(pEn3Seq)}').grid(row = 12, column = 0, columnspan = 2)
        Label(resWin, text = f'      Nearest Neighbor Method: ').grid(row = 13, column = 0)
        Label(resWin, text = f'               Wallace Method: ').grid(row = 14, column = 0)
        Label(resWin, text = f'                   GC% Method: \n').grid(row = 15, column = 0)
        Label(resWin, text = f' {round(nnM, 1)}').grid(row = 13, column = 1)
        Label(resWin, text = f' {round(float(wallace), 1)}').grid(row = 14, column = 1)
        Label(resWin, text = f' {round(gcMethod, 1)}\n').grid(row = 15, column = 1)

    if pEn4Seq:
        noA = 0
        noT = 0
        noC = 0
        noG = 0
        for i in pEn4Seq:
            if i == 'A':
                noA += 1
            elif i == 'T':
                noT += 1
            elif i == 'C':
                noC += 1
            elif i == 'G':
                noG += 1
        gcPer = (noC+noG)*100/(noA+noT+noC+noG)

        wallace = 2*noA+2*noT+4*noC+4*noG
        gcMethod = 81.5+16.6*math.log10(saltConc/1000)+41*gcPer/100-primerConc/(noA+noT+noC+noG)  

        sumH = 0
        sumS = 0
        neiPair = [pEn4Seq[j:j+2] for j in range(len(pEn4Seq)-1)]
        for k in neiPair:
            sumH += paraHS[k][0]
            sumS += paraHS[k][1]
        
        nnM = (1000*sumH/(-10.8+sumS+1.987*math.log(primerConc/4000000000)))-273.15+16.6*math.log10(saltConc/1000)

        pEn4Seq2 = StringVar()
        pEn4Seq2.set(pEn4Seq)

        Label(resWin, text = f'(4)  {pEn4Seq}', font = ('Helvetica', 15, 'bold')).grid(row = 16, column = 0, columnspan = 2)
        Label(resWin, text = f'GC = {round(gcPer, 1)}%, Length = {len(pEn4Seq)}').grid(row = 17, column = 0, columnspan = 2)
        Label(resWin, text = f'      Nearest Neighbor Method: ').grid(row = 18, column = 0)
        Label(resWin, text = f'               Wallace Method: ').grid(row = 19, column = 0)
        Label(resWin, text = f'                   GC% Method: \n').grid(row = 20, column = 0)
        Label(resWin, text = f' {round(nnM, 1)}').grid(row = 18, column = 1)
        Label(resWin, text = f' {round(float(wallace), 1)}').grid(row = 19, column = 1)
        Label(resWin, text = f' {round(gcMethod, 1)}\n').grid(row = 20, column = 1)

    if pEn5Seq:
        noA = 0
        noT = 0
        noC = 0
        noG = 0
        for i in pEn5Seq:
            if i == 'A':
                noA += 1
            elif i == 'T':
                noT += 1
            elif i == 'C':
                noC += 1
            elif i == 'G':
                noG += 1
        gcPer = (noC+noG)*100/(noA+noT+noC+noG)

        wallace = 2*noA+2*noT+4*noC+4*noG
        gcMethod = 81.5+16.6*math.log10(saltConc/1000)+41*gcPer/100-primerConc/(noA+noT+noC+noG)  

        sumH = 0
        sumS = 0
        neiPair = [pEn5Seq[j:j+2] for j in range(len(pEn5Seq)-1)]
        for k in neiPair:
            sumH += paraHS[k][0]
            sumS += paraHS[k][1]
        
        nnM = (1000*sumH/(-10.8+sumS+1.987*math.log(primerConc/4000000000)))-273.15+16.6*math.log10(saltConc/1000)

        pEn5Seq2 = StringVar()
        pEn5Seq2.set(pEn5Seq)

        Label(resWin, text = f'(5)  {pEn5Seq}', font = ('Helvetica', 15, 'bold')).grid(row = 21, column = 0, columnspan = 2)
        Label(resWin, text = f'GC = {round(gcPer, 1)}%, Length = {len(pEn5Seq)}').grid(row = 22, column = 0, columnspan = 2)
        Label(resWin, text = f'      Nearest Neighbor Method: ').grid(row = 23, column = 0)
        Label(resWin, text = f'               Wallace Method: ').grid(row = 24, column = 0)
        Label(resWin, text = f'                   GC% Method: \n').grid(row = 25, column = 0)
        Label(resWin, text = f' {round(nnM, 1)}').grid(row = 23, column = 1)
        Label(resWin, text = f' {round(float(wallace), 1)}').grid(row = 24, column = 1)
        Label(resWin, text = f' {round(gcMethod, 1)}\n').grid(row = 25, column = 1)

    if pEn6Seq:
        noA = 0
        noT = 0
        noC = 0
        noG = 0
        for i in pEn6Seq:
            if i == 'A':
                noA += 1
            elif i == 'T':
                noT += 1
            elif i == 'C':
                noC += 1
            elif i == 'G':
                noG += 1
        gcPer = (noC+noG)*100/(noA+noT+noC+noG)

        wallace = 2*noA+2*noT+4*noC+4*noG
        gcMethod = 81.5+16.6*math.log10(saltConc/1000)+41*gcPer/100-primerConc/(noA+noT+noC+noG)  

        sumH = 0
        sumS = 0
        neiPair = [pEn6Seq[j:j+2] for j in range(len(pEn6Seq)-1)]
        for k in neiPair:
            sumH += paraHS[k][0]
            sumS += paraHS[k][1]
        
        nnM = (1000*sumH/(-10.8+sumS+1.987*math.log(primerConc/4000000000)))-273.15+16.6*math.log10(saltConc/1000)

        pEn6Seq2 = StringVar()
        pEn6Seq2.set(pEn6Seq)

        Label(resWin, text = f'(6)  {pEn6Seq}', font = ('Helvetica', 15, 'bold')).grid(row = 26, column = 0, columnspan = 2)
        Label(resWin, text = f'GC = {round(gcPer, 1)}%, Length = {len(pEn6Seq)}').grid(row = 27, column = 0, columnspan = 2)
        Label(resWin, text = f'      Nearest Neighbor Method: ').grid(row = 28, column = 0)
        Label(resWin, text = f'               Wallace Method: ').grid(row = 29, column = 0)
        Label(resWin, text = f'                   GC% Method: \n').grid(row = 30, column = 0)
        Label(resWin, text = f' {round(nnM, 1)}').grid(row = 28, column = 1)
        Label(resWin, text = f' {round(float(wallace), 1)}').grid(row = 29, column = 1)
        Label(resWin, text = f' {round(gcMethod, 1)}\n').grid(row = 30, column = 1)

def openweb():
    webbrowser.open('https://wongzit.github.io/program/tmcalc', new = 1)

paraHS = {
    'AA':[-9.1, -24],
    'AT':[-8.6, -23.9],
    'AC':[-6.5, -17.3],
    'AG':[-7.8, -20.8],
    'TA':[-6, -16.9],
    'TT':[-9.1, -24],
    'TC':[-5.6, -13.5],
    'TG':[-5.8, -12.9],
    'CA':[-5.8, -12.9],
    'CT':[-7.8, -20.8],
    'CC':[-11, -26.6],
    'CG':[-11.9, -27.8],
    'GA':[-5.6, -13.5],
    'GT':[-6.5, -17.3],
    'GC':[-11.1, -26.7],
    'GG':[-11, -26.6]
}


pEn1Val = StringVar()
pEn2Val = StringVar()
pEn3Val = StringVar()
pEn4Val = StringVar()
pEn5Val = StringVar()
pEn6Val = StringVar()

pEn1Val.set('')
pEn2Val.set('')
pEn3Val.set('')
pEn4Val.set('')
pEn5Val.set('')
pEn6Val.set('')

# Set the initial concentration of salt and primer
saltIni = IntVar()
saltIni.set(50)
primerIni = IntVar()
primerIni.set(500)

# Section for initial concentration of salt and primer, the concentration value
# could only be set to INT
inputFrame = LabelFrame(root, borderwidth = 0, highlightthickness = 0)
inputFrame.grid(row = 2, column = 0, columnspan = 5, sticky = W + E)
Label(inputFrame, text = '     --------- Concentration ---------', font = ('Helvetica', 15, 'bold')).grid(row = 0, column = 0, columnspan = 5)
Label(inputFrame, text = 'Salt =').grid(row = 1, column = 0)
slatEntry = Entry(inputFrame, textvariable = saltIni, width = 6).grid(row = 1, column = 1)
Label(inputFrame, text = 'mM,   Primer =').grid(row = 1, column = 2)
primerEntry = Entry(inputFrame, textvariable = primerIni, width = 6).grid(row = 1, column = 3)
Label(inputFrame, text = 'nM').grid(row = 1, column = 4)

# Section for primer sequences
Label(inputFrame, text = '\n     -------- Primer Sequence --------', font = ('Helvetica', 15, 'bold')).grid(row = 2, column = 0, columnspan = 5)
Label(inputFrame, text = '(1)', font = ('Helvetica', 13, 'bold')).grid(row = 3, column = 0)
pEn1 = Entry(inputFrame, textvariable = pEn1Val, width = 32).grid(row = 3, column = 1, columnspan = 4)
Label(inputFrame, text = '(2)', font = ('Helvetica', 13, 'bold')).grid(row = 4, column = 0)
pEn2 = Entry(inputFrame, textvariable = pEn2Val, width = 32).grid(row = 4, column = 1, columnspan = 4)
Label(inputFrame, text = '(3)', font = ('Helvetica', 13, 'bold')).grid(row = 5, column = 0)
pEn3 = Entry(inputFrame, textvariable = pEn3Val, width = 32).grid(row = 5, column = 1, columnspan = 4)
Label(inputFrame, text = '(4)', font = ('Helvetica', 13, 'bold')).grid(row = 6, column = 0)
pEn4 = Entry(inputFrame, textvariable = pEn4Val, width = 32).grid(row = 6, column = 1, columnspan = 4)
Label(inputFrame, text = '(5)', font = ('Helvetica', 13, 'bold')).grid(row = 7, column = 0)
pEn5 = Entry(inputFrame, textvariable = pEn5Val, width = 32).grid(row = 7, column = 1, columnspan = 4)
Label(inputFrame, text = '(6)', font = ('Helvetica', 13, 'bold')).grid(row = 8, column = 0)
pEn6 = Entry(inputFrame, textvariable = pEn6Val, width = 32).grid(row = 8, column = 1, columnspan = 4)

# Icon file
calcIcon = PhotoImage(file = r'assets/read_icon.png')
webIcon = PhotoImage(file = r'assets/web_icon.png')
quitIcon = PhotoImage(file = r'assets/quit_icon.png')

# Button defination
Label(root, text = '  ').grid(row = 9, column = 0)
calcButton = Button(root, image = calcIcon, padx = 20, pady = 6, command = calctm).grid(row = 10, column = 0)
webButton = Button(root, image = webIcon, padx = 20, pady = 6, command = openweb).grid(row = 10, column = 2)
quitButton = Button(root, image = quitIcon, padx = 20, pady = 8, command = sys.exit).grid(row = 10, column = 4)

# Section for buttons
Label(root, text = 'Calculate', font = ('Helvetica', 13, 'bold')).grid(row = 11, column = 0)
Label(root, text = 'Help', font = ('Helvetica', 13, 'bold')).grid(row = 11, column = 2)
Label(root, text = 'Quit', font = ('Helvetica', 13, 'bold')).grid(row = 11, column = 4)

# Copyright information
Label(root, text = 'Copyright © 2022, Zhe Wang at Research group of  \nReaction Organic Chemistry, Hiroshima University.  ', bd = 1, width = 25, relief = SUNKEN, anchor = E, bg = 'old lace').grid(row = 12, column = 0, columnspan = 5, sticky = W + E)

root.mainloop()

import math

# Program information section
print("\n                         *      T m . C a l c      *                         ")
print("")
print("                   --- A melting temperature calculator ---                  ")
print("                         - Version 1.0.0 / RELEASE -                         ")
print("")
print("             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-             ")
print("                 Developed by Zhe Wang, Hiroshima University                 ")
print("                   https://wongzit.github.io/program/tmcalc                  ")
print("                           Last update: 2022-01-23                           ")
print("             -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-             ")

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

concNa = 50 # mM
concPr = 500 # nM

while True:
	print("\n===================================")
	print("       Concentration Setting       ")
	print("-----------------------------------")
	print(f"   1 - Salt conc. = {concNa} mM")
	print(f"   2 - Primer conc. = {concPr} nM")
	print("===================================")
	print("Input menu number to modify concentration, or input primer sequences:")
	usrInp = input("e.g.: ATCGGACTAGACGAT,AGGGTCTTACAGAGCT,GGGCTTTAGAATAGA\n")
	if usrInp == '1':
		while True:
			try:
				concNa = float(input("Input the concentration of salt, in mM:"))
				break
			except ValueError:
				print("\nInput error, please input a number!")
				continue

	elif usrInp == '2':
		while True:
			try:
				concPr = float(input("Input the concentration of primer, in nM:"))
				break
			except ValueError:
				print("\nInput error, please input a number!")
				continue

	else:
		break

seq = usrInp.upper().split(',')
noSeq = len(seq)

for curSeq in seq:
	print(f"\nSequence: {curSeq.strip()}")
	noA = 0
	noT = 0
	noC = 0
	noG = 0
	curSeq = curSeq.strip()
	for i in curSeq:
		if i == 'A':
			noA += 1
		elif i == 'T':
			noT += 1
		elif i == 'C':
			noC += 1
		elif i == 'G':
			noG += 1
	gcPer = (noC+noG)*100/(noA+noT+noC+noG)
	print(f'GC = {round(gcPer, 1)}%, Length = {len(curSeq)}')

	wallace = 2*noA+2*noT+4*noC+4*noG
	gcMethod = 81.5+16.6*math.log10(concNa/1000)+41*gcPer/100-concPr/(noA+noT+noC+noG)

	sumH = 0
	sumS = 0
	neiPair = [curSeq[j:j+2] for j in range(len(curSeq)-1)]
	for k in neiPair:
		sumH += paraHS[k][0]
		sumS += paraHS[k][1]
	
	nnM = (1000*sumH/(-10.8+sumS+1.987*math.log(concPr/4000000000)))-273.15+16.6*math.log10(concNa/1000)
	print(f'---------- Melting Temperature ----------')
	print(f'      Nearest Neighbor Method: {round(nnM, 1)}')
	print(f'               Wallace Method: {round(float(wallace), 1)}')
	print(f'                   GC% Method: {round(gcMethod, 1)}')

print("")

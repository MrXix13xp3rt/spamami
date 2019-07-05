import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;        SPAMAMI                   ;
		;---------------------------;
		; Author :    MrXix13xp3rt   ;
		; Contact : 082367193770  ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
1. Spam Teri
2. Spam Grab
3. Spam HOOQ
4. Spam OYO
5. Spam Telkampret
6. Spam Gratis
""")
		pilih=int(input('/:MrXix13xp3rt'))
		if pilih == 1:
			import src.sms
		elif pilih == 2:
			import src.grab
		elif pilih == 3:
			import src.hooq
		elif pilih == 4:
			import src.oyo
		elif pilih == 5:
			print("""
		;;;;;;;;;;;;;;;;;;;
		; Spam Telkampret ;
		;;;;;;;;;;;;;;;;;;;
1. Spam Telkampret V1
2. Spam Telkampret V2
""")
			pilihlagi=int(input('/:MrXix13xp3rt'))
			if pilihlagi == 1:
				import src.telnyet
			elif pilihlagi == 2:
				import src.telnyet2
			else: print("[!] Menu nya apa(o)");self.menu()
		elif pilih == 6:
			import src.gratis
		else: print("[!] Menu Nya Apa(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))

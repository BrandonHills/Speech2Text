import os


class TrainKaldi:
	
	def AddData(self, audio_paths, texts, durations, numDuplicates):
		
		numFiles = len(audio_paths)

		#Spk2Gender
		with open('spk2gender','r') as file:
			spk2gender=file.readlines()
		spk2genderADD=['addition-1 m\n']

		os.system('rm spk2gender')
		spk2genderADD.extend(spk2gender)
		with open('spk2gender','w') as f:
			for d in spk2genderADD:
				f.write(d)

		#Utt2Dur
		with open('utt2dur','r') as file:
			utt2dur=file.readlines()
		utt2durADD=[]
		D=durations
		for FILE in range(numFiles):
			for n in range(numDuplicates):
				if n < 10:
					s='00'+str(n)
				elif n < 100:
					s='0'+str(n)
				else:
					s=str(n)
				utt2durADD.append('addition-1-'+s+str(FILE) + ' ' + str(D[FILE]) + '\n')
		utt2durADD.extend(utt2dur)

		os.system('rm utt2dur')
		with open('utt2dur','w') as f:
			for d in utt2durADD:
				f.write(d)


		#Text
		with open ('text', 'r') as file:
			text=file.readlines()
		textADD=[]

		T=texts

		for FILE in range(numFiles):
			for n in range(numDuplicates):
				if n < 10:
					s = '00'+str(n)
				elif n < 100:
					s='0'+str(n)
				else:
					s=str(n)
				textADD.append('addition-1-'+s+str(FILE) + ' ' + T[FILE] + '\n') 
		textADD.extend(text)

		os.system('rm text')
		with open('text','w') as f:
			for d in textADD:
				f.write(d)


		#Utt2Spk
		with open ('utt2spk', 'r') as file:
			utt2spk=file.readlines()
		utt2spkADD=[]
		for FILE in range(numFiles):
			for n in range(numDuplicates):
				if n < 10:
					s = '00'+str(n)
				elif n < 100:
					s = '0'+str(n)
				else:
					s=str(n)
				utt2spkADD.append('addition-1-'+ s + str(FILE) + ' addition-1\n')

		utt2spkADD.extend(utt2spk)
		os.system('rm utt2spk')
		with open('utt2spk', 'w') as f:
			 for d in utt2spkADD:
				f.write(d)


		# Spk2Utt
		with open('spk2utt', 'r') as file:
			spk2utt=file.readlines()
		spk2uttADD = []
		string = 'addition-1'
		for FILE in range(numFiles):
	
			for n in range(numDuplicates):
				if n < 10:
					s = '00'+str(n)
				elif n < 100:
					s='0'+str(n)
				else:
					s=str(n)
				string += " addition-1-" + s + str(FILE)
		string += ' \n'
		spk2uttADD.append(string)
		spk2uttADD.extend(spk2utt)

		os.system('rm spk2utt')
		with open ('spk2utt',"w") as f:
			for d in spk2uttADD:
				f.write(d)


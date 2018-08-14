import os
import sys
import linecache
import numpy as np


def main():

	"""INFERENCE PIPELINE DEMO"""
	if 0 == 1:
		s2t = RecognizeSpeech()
		print("RETURN: " + s2t.infer(s2t.dirPath +"Speech2Text/demo.flac", "demo.flac"))
	
	"""TRAINING PIPELINE DEMO"""
	if 0 == 0:

		s2t = RecognizeSpeech()

		audio_paths = ["data/LibriSpeech/train-clean-100/addition/1/addition-1-0000.flac",
		"data/LibriSpeech/train-clean-100/addition/1/addition-1-0001.flac",
		"data/LibriSpeech/train-clean-100/addition/1/addition-1-0002.flac"]

		texts = ["KINDLY CONTACT THE AHD AND DO THE NEEDFUL",
		"PLEASE CONTACT THE AHD AND DO THE NEEDFUL",
		"KINDLY REMIND THE AHD TO RESPOND TO MY REQUEST"]

		durations = [.5,.5,.6]

		numDuplicates = 100

		s2t.train(audio_paths, texts, durations, numDuplicates)

	""" DATA PREPARATION DEMO"""
	if 0 == 1:
		s2t = RecognizeSpeech()
		s2t.prepareData(s2t.dirPath +"Speech2Text/audio/output_16000.flac")
		s2t.runTest()
		print(s2t.returnText())



class RecognizeSpeech:

	def __init__(self):
		self.dirPath = "/home/eundlpoc002adm/brandon-s2t/kaldi/egs/librispeech/s5/"
		self.data = self.dirPath + "data/recognizeWav/"
		self.output = self.dirPath + "exp/tri2b/decode_nosp_tgsmall_recognizeWav/log/decode.1.log"




	def prepareData(self, audioPath):
		
		print("Creating wav.scp file")
		# Create wav.scp file

		location = self.data + 'wav.scp'
		os.system("rm " + location)

		with open(location, 'w+') as the_file:
			the_file.write('input-0000 flac -c -d -s ' + audioPath + " |")

		print("Created wav.scp file in " + location)


	def runTest(self):
		print("running runChange.sh")
		os.chdir(self.dirPath)
		os.system(self.dirPath + "runChange.sh")

	def returnText(self):

		record = linecache.getline(self.output, 11)

		print(record[11:])

		linecache.clearcache()

		return record[11:]

	def convertToFLAC(self, path):
		if path[:-5] == ".flac":
			print("COMMAND: ffmpeg -i " + path + " -ar 16000 " + path[:-5] +".flac")
			os.system("ffmpeg -i " + path + " -sample_fmt s16 -ar 16000 " + path[:-5] +".flac")
		elif path[:-4] == ".mp3" or path[:-4] == ".wav":
			print("COMMAND: ffmpeg -i " + path + " -ar 16000 " + path[:-4] +".flac")
			os.system("ffmpeg -i " + path + " -sample_fmt s16 -ar 16000 " + path[:-4] +".flac")
		else:
			print("COMMAND: ffmpeg -i " + path + " -ar 16000 " + path + ".flac")
			os.system("ffmpeg -i " + path + " -sample_fmt s16 -ar 16000 " + path +".flac")
		

	def infer(self, audio_path, name):
		self.moveLocation = self.dirPath + 'audio2infer/'
		self.outputLocation = self.dirPath + 'audio2infer/output.flac'

		# Removing previous directory
		os.system('rm -R ' + self.dirPath + 'audio2infer/')
		os.system('mkdir ' + self.dirPath + 'audio2infer/')


		os.system('cp -R '+audio_path+' '+self.moveLocation+name)

		self.convertToFLAC(self.moveLocation+name)

		# self.prepareData(self.outputLocation)
		self.prepareData(self.moveLocation+name)

		self.runTest()

		return self.returnText()

	def Train(self, audio_paths, texts, durations, numDuplicates):

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

















	def train(self, audio_paths, texts, durations, numDuplicates):
		os.chdir(self.dirPath)
		os.system(self.dirPath + "runPrepare.sh")







if __name__ == "__main__":
	main()














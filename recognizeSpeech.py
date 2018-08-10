import os
import sys
import linecache
import numpy as np


def main():
	if 0 == 0:
		s2t = RecognizeSpeech()
		print("RETURN: " + s2t.infer(s2t.dirPath +"Speech2Text/Carnegie.mp3"))
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
		

	def infer(self, audio_path):
		self.moveLocation = self.dirPath + 'audio2infer/output'
		self.outputLocation = self.dirPath + 'audio2infer/output.flac'

		# Removing previous directory
		os.system('rm -R ' + self.dirPath + 'audio2infer/')
		os.system('mkdir ' + self.dirPath + 'audio2infer/')


		os.system('cp -R '+audio_path+' '+self.moveLocation)

		self.convertToFLAC(self.moveLocation)

		self.prepareData(self.outputLocation)

		self.runTest()

		return self.returnText()





if __name__ == "__main__":
	main()














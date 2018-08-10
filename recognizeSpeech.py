import os
import sys
import linecache
import numpy as np


def main():
	if 0 == 1:
		s2t = RecognizeSpeech()
		print("RETURN: " + s2t.infer(s2t.dirPath +"data/recognizeWav/inputData/input19.flac"))
	if 0 == 0:
		s2t = RecognizeSpeech()
		s2t.prepareData(s2t.dirPath +"Speech2Text/audio/output.flac")



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

	def convertMP3toFLAC(self, path):
		print("COMMAND" + "ffmpeg -i " + path + " -ar 16000 " + path[:-4] +".flac")
		os.system("ffmpeg -i " + path + " -ar 16000 " + path[:-4] +".flac")

	def infer(self, audio_path):
		self.mp3Location = self.dirPath + 'audio2infer/' + 'input.mp3'
		self.flacLocation = self.dirPath + 'audio2infer/' + 'input.flac'

		os.system('rm -R ' + self.dirPath + 'audio2infer/')
		os.system('mkdir ' + self.dirPath + 'audio2infer/')
		os.system('cp -R '+audio_path+' '+self.mp3Location)

		self.convertMP3toFLAC(self.mp3Location)

		self.prepareData(self.flacLocation)

		self.runTest()

		return self.returnText()





if __name__ == "__main__":
	main()














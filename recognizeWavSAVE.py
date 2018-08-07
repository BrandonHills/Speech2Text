import os
import sys
import linecache
import librosa
import numpy as np
import matplotlib.pyplot as plt
import random


def main():

	if 0 == 1:
		s2t = RecognizeWav("/home/eundlpoc002adm/brandon-s2t/kaldi/egs/librispeech/s5/", "data/recognizeWav/")
		s2t.convertMP3toFLAC(s2t.dirPath + "Speech2Text/audio/Kindly_Remind_the_AHD_to_respond_to_my_request.mp3")

	if 0 == 1:
		for i in range(0,1):
			s2t = RecognizeWav("/home/eundlpoc002adm/brandon-s2t/kaldi/egs/librispeech/s5/", "data/recognizeWav/")

			s2t.prepareData(s2t.dirPath +"data/recognizeWav/inputData/input20.flac")

			s2t.runTest()

			s2t.returnText()
	if 1 == 1:
		s2t = RecognizeWav("/home/eundlpoc002adm/brandon-s2t/kaldi/egs/librispeech/s5/", "data/recognizeWav/")
		
		s2t.duplicateData("/Users/HillOfFlame/NLP_InfoSys/Speech2Text/audio/output.flac", "/Users/HillOfFlame/NLP_InfoSys/Speech2Text/audio/duplicated/", 5)



class RecognizeWav:

	def __init__(self, dirPath, dataPath):
		self.dirPath = dirPath
		self.data = dataPath
		self.output = "exp/tri2b/decode_nosp_tgsmall_recognizeWav/log/decode.1.log"


	def prepareData(self, audioPath):
		
		print("Creating wav.scp file")
		# Create wav.scp file

		location = self.dirPath + self.data + 'wav.scp'
		os.system("rm " + location)

		with open(location, 'w+') as the_file:
			the_file.write('input-0000 flac -c -d -s ' + audioPath + " |")

		print("Created wav.scp file in " + location)


	def runTest(self):
		print("running runChange.sh")
		os.chdir(self.dirPath)
		os.system(self.dirPath + "runChange.sh")

	def returnText(self):

		
		record = linecache.getline(self.dirPath + self.output, 11)

		print(record[11:])

		linecache.clearcache()

	def convertMP3toFLAC(self, path):
		print("COMMAND" + "ffmpeg -i " + path + " -ar 16000 " + path[:-4] +".flac")
		os.system("ffmpeg -i " + path + " -ar 16000 " + path[:-4] +".flac")




if __name__ == "__main__":
	main()














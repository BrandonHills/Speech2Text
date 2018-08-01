import os
import sys
import linecache

def main():
	s2t = RecognizeWav("/home/eundlpoc002adm/brandon-s2t/kaldi/egs/librispeech/s5/", "data/recognizeWav/")

	s2t.prepareData(s2t.dirPath +"data/recognizeWav/inputData/input1.flac")

	s2t.runTest()

	s2t.returnText()

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

		print(linecache.getline(self.dirPath + self.output, 11))




if __name__ == "__main__":
	main()



1089-134686-0007











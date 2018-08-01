import os
import sys

def main():
	s2t = RecognizeWav("/home/eundlpoc002adm/brandon-s2t/kaldi/egs/librispeech/s5/", "data/recognizeWav/")

	s2t.prepareData(s2t.dirPath +"data/recognizeWav/inputData/input.flac")

	s2t.runTest()

class RecognizeWav:

	def __init__(self, dirPath, dataPath):
		self.dirPath = dirPath
		self.data = dataPath


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
		os.system(self.dirPath + "jump.sh")



if __name__ == "__main__":
	main()





import pandas as pd
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

class mlforrank(object):
	"""docstring for mlforrank"""
	def __init__(self, dataframe):
		super(mlforrank, self).__init__()
		self.dataframe = dataframe
	def data_extractor(self):
		self.x = self.dataframe.iloc[:-1,:-1]
		print(self.x)
		self.y = self.dataframe.iloc[:-1,[-1]]
		print(self.y)
		self.x_test = self.dataframe.iloc[-1,:-1]
		print(self.x_test)
	def estimator(self):
		self.data_extractor()
		C=1
		kernel='rbf'
		gamma=0.01
		classifier = SVC(C=C, kernel=kernel, gamma=gamma)
		classifier.fit(self.x,self.y)
		print(self.x_test.values)
		pred_y = classifier.predict(self.x_test.values.reshape([1,-1]))

		return pred_y

def main():
	df=pd.read_csv("test.csv")
	print(df)
	rank = mlforrank(df)
	print(rank.estimator())
if __name__ == '__main__':
	main()
		
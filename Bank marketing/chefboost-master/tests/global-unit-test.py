import pandas as pd
import sys
from chefboost import Chefboost as cb

#----------------------------------------------
parallelism_cases = [False]

if __name__ == '__main__':

	for enableParallelism in parallelism_cases:
		
		print("*************************")
		print("enableParallelism is set to ",enableParallelism)
		print("*************************")
		
		print("ID3 for nominal features and target:")
		config = {'algorithm': 'ID3', 'enableParallelism': enableParallelism}
		model = cb.fit(pd.read_csv("dataset/golf.txt"), config)
		
		cb.save_model(model)
		print("built model is saved to model.pkl")
		
		restored_model = cb.load_model("model.pkl")
		print("built model is restored from model.pkl")
		
		instance = ['Sunny', 'Hot', 'High', 'Weak']
		prediction = cb.predict(restored_model, instance)
		
		print("prediction for ", instance, "is ", prediction)

		print("-------------------------")
		
		print("ID3 for nominal/numeric features and target:")
		config = {'algorithm': 'ID3', 'enableParallelism': enableParallelism}
		model = cb.fit(pd.read_csv("dataset/golf2.txt"), config)
		
		instance = ['Sunny', 85, 85, 'Weak']
		prediction = cb.predict(restored_model, instance)
		print("prediction for ", instance, "is ", prediction)

		print("-------------------------")
		
		print("C4.5 for nominal/numeric features and target:")
		config = {'algorithm': 'C4.5', 'enableParallelism': enableParallelism}
		cb.fit(pd.read_csv("dataset/golf2.txt"), config)

		print("-------------------------")

		print("CART for nominal/numeric features and target:")
		config = {'algorithm': 'CART', 'enableParallelism': enableParallelism}
		cb.fit(pd.read_csv("dataset/golf2.txt"), config)

		print("-------------------------")

		print("regression tree for nominal features, numeric target")
		config = {'algorithm': 'Regression', 'enableParallelism': enableParallelism}
		cb.fit(pd.read_csv("dataset/golf3.txt"), config)

		print("-------------------------")

		print("regression tree for nominal/numeric features, numeric target")
		config = {'algorithm': 'Regression', 'enableParallelism': enableParallelism}
		cb.fit(pd.read_csv("dataset/golf4.txt"), config)

		print("-------------------------")

		print("algorithm must be regression tree for numetic target. set any other algorithm.")
		config = {'algorithm': 'ID3', 'enableParallelism': enableParallelism}
		cb.fit(pd.read_csv("dataset/golf4.txt"), config)

		print("-------------------------")

		print("ID3 for nominal features and target (large data set)")
		config = {'algorithm': 'ID3', 'enableParallelism': enableParallelism}
		model = cb.fit(pd.read_csv("dataset/car.data", names=["buying", "maint", "doors", "persons", "lug_boot", "safety", "Decision"]), config)
		
		instance = ['vhigh','vhigh',2,'2','small','low']
		prediction = cb.predict(model, instance)
		print(prediction)
		
		instance = ['high','high',4,'more','big','high']
		prediction = cb.predict(model, instance)
		print(prediction)

		print("-------------------------")

		print("C4.5 for nominal features and target (large data set)")
		config = {'algorithm': 'C4.5', 'enableParallelism': enableParallelism}
		cb.fit(pd.read_csv("dataset/car.data", names=["buying", "maint", "doors", "persons", "lug_boot", "safety", "Decision"]), config)

		print("-------------------------")

		print("CART for nominal features and target (large data set)")
		config = {'algorithm': 'CART', 'enableParallelism': enableParallelism}
		cb.fit(pd.read_csv("dataset/car.data", names=["buying", "maint", "doors", "persons", "lug_boot", "safety", "Decision"]), config)
		
		print("-------------------------")
		
		print("Adaboost")
		config = {'algorithm': 'ID3', 'enableAdaboost': True, 'enableParallelism': False}
		model = cb.fit(pd.read_csv("dataset/adaboost.txt"), config)
		
		instance = [4, 3.5]
		#prediction = cb.predict(model, instance)
		#print("prediction for ",instance," is ",prediction)
		
		print("-------------------------")
		
		print("Regular GBM")
		config = {'algorithm': 'CART', 'enableGBM': True, 'epochs': 10, 'learning_rate': 1, 'enableParallelism': enableParallelism}
		model = cb.fit(pd.read_csv("dataset/golf4.txt"), config)
		
		instance = ['Sunny',85,85,'Weak']
		prediction = cb.predict(model, instance)
		print("prediction for ",instance," is ",prediction)

		print("-------------------------")
		
		print("GBM for classification")
		config = {'algorithm': 'ID3', 'enableGBM': True, 'epochs': 10, 'learning_rate': 1, 'enableParallelism': enableParallelism}
		model = cb.fit(pd.read_csv("dataset/iris.data", names=["Sepal length", "Sepal width", "Petal length", "Petal width", "Decision"]), config)
		
		instance = [7.0,3.2,4.7,1.4]
		prediction = cb.predict(model, instance)
		print("prediction for ",instance," is ",prediction)

		print("-------------------------")

		print("Random forest")
		config = {'algorithm': 'ID3', 'enableRandomForest': True, 'num_of_trees': 5, 'enableMultitasking': False, 'enableParallelism': enableParallelism}
		model = cb.fit(pd.read_csv("dataset/car.data", names=["buying", "maint", "doors", "persons", "lug_boot", "safety", "Decision"]), config)
		
		instance = ['vhigh','vhigh',2,'2','small','low']
		
		prediction = cb.predict(model, instance)
		print("prediction for ",instance," is ",prediction)
		
		instance = ['high','high',4,'more','big','high']

		prediction = cb.predict(model, instance)
		print("prediction for ",instance," is ",prediction)
		
		print("-------------------------")

	print("-------------------------")
	print("unit tests completed successfully...")

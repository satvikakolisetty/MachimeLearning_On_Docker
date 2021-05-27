import joblib as jb
model=jb.load('salaryPred.pk1')
model.predict([[6.0]])
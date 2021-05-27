import joblib as jb
model=jb.load('salaryPred.pk1')
print()
print(model.predict([[6.0]]))

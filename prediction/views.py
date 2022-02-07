from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def predict(request):
    return render(request, 'predict.html')


def result(request):
    data = pd.read_csv(r"train.csv")
    X = data.drop("price_range", axis=1)
    Y = data['price_range']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    val13 = float(request.GET['n13'])
    val14 = float(request.GET['n14'])
    val15 = float(request.GET['n15'])
    val16 = float(request.GET['n16'])
    val17 = float(request.GET['n17'])
    val18 = float(request.GET['n18'])
    val19 = float(request.GET['n19'])
    val20 = float(request.GET['n20'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9,
                           val10, val11, val12, val13, val14, val15, val16, val17, val18, val19, val20]])

    if pred == [0]:
        result2 = "Mobile price will lie in low price range"

    elif pred == [1]:
        result2 = "Mobile price will lie in medium price range"
    elif pred == [2]:
        result2 = "Mobile price will lie in high price range"
    else:
        result2 = "Mobile price will lie in very high price range"

    if val6 == 0:
        result3 = "NO"
    else:
        result3 = "YES"


    context = {"result2" : result2, "val1" : int(val1), "val6" : result3, "val7" : int(val7), "val10" : int(val10), "val14" : int(val14)}
    return render(request, 'result.html', context)

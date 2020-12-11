# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

base = pd.read_csv('credit_card_clients.csv', header = 1)

#somar as dividas
base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3'] + base['BILL_AMT4'] + base['BILL_AMT5'] + base['BILL_AMT6']

X = base.iloc[:,[1,25]].values

scaler = StandardScaler()
X = scaler.fit_transform(X)

wcss = []
for i in range (1, 11):
	kmeans = KMeans(n_clusters = i, random_state = 0)
	kmeans.fit(X)
	wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.xlabel('Numero de clusters')
plt.ylabel('WCSS')

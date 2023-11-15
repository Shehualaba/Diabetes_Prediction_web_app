#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MultiLabelEncoder:
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_encoded = X.copy()
        for col in range(X.shape[1]):
            le = LabelEncoder()
            X_encoded[col] = le.fit_transform(X[col])
        return X_encoded


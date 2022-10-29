#!/usr/bin/python3

# Комментарий из VS Code

from catboost.datasets import titanic

train, test = titanic()

train.to_csv("../../data/raw/train.csv", index=False)

test.to_csv("../../data/raw/test.csv", index=False)

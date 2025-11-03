import pandas as pd, math
from collections import Counter
from pprint import pprint

def id3(df, target, attributes, default=None):
    counts = Counter(df[target])
    if len(counts) == 1: return next(iter(counts))
    if not attributes: return default
    default = max(counts, key=counts.get)
    def entropy(lst):
        probs = [x/len(lst) for x in Counter(lst).values()]
        return sum(-p*math.log(p,2) for p in probs if p>0)
    def info_gain(attr):
        total = len(df)
        weighted = sum((len(sub)/total)*entropy(sub[target]) for _,sub in df.groupby(attr))
        return entropy(df[target]) - weighted
    best = max(attributes, key=info_gain)
    tree = {best:{}}
    remaining = [a for a in attributes if a!=best]
    for val, sub in df.groupby(best):
        tree[best][val] = id3(sub, target, remaining, default)
    return tree

data = {
    'Outlook':['Sunny','Sunny','Overcast','Rain','Rain','Overcast'],
    'Humidity':['High','High','High','High','Normal','Normal'],
    'Wind':['Weak','Strong','Weak','Weak','Weak','Strong'],
    'PlayTennis':['No','No','Yes','Yes','Yes','Yes']
}

df = pd.DataFrame(data)
attrs = list(df.columns.drop('PlayTennis'))
tree = id3(df,'PlayTennis',attrs)
print("The Resultant Decision Tree is:")
pprint(tree)

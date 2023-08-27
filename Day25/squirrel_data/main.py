import pandas

data = pandas.read_csv("squirrel_data.csv")

# print(data)

squirrel_count = data.groupby("Primary Fur Color").size().reset_index(name='counts')
squirrel_count.to_csv("squirrel_count.csv")
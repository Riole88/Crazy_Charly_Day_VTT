import getData
from src.RecuitSimule import switchObject

d = getData
d.get_data()
abonnes = d.getAbonnes()
articles = d.getArticles()
massMax = d.getMassMax()
print(switchObject())




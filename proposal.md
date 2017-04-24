# Capstone project proposal - document clustering

## 1. What is the problem you want to solve

Find similarities between articles about terorrist attacks. Identify common expressions and language used to report on the attacks and find out if there are differencies in how different attacks are being covered. See if there are any meaningful groups of articles based on the place of an attack as mentioned in the [Paris, Beirut, and the Language Used to Describe Terrorism](https://www.theatlantic.com/international/archive/2015/11/paris-beirut-media-coverage/416457/).


## 2. Who is your client and why do they care about this problem? In other words, what will your client DO or DECIDE based on your analysis that they wouldn’t have otherwise?

Our studio has already developed a visualisation part the engine to display latest news on globe, with articles forming a force-directed graph. This project should be driving the clustering part of the already existing project.

More generally, this project is conceived as proof-of-concept work to create a text clustering system. This system will drive custom made data visualisations. The code developed for the capstone project should be reusable for text documents from different sources and on different topics.


## 3. What data are you going to use for this? How will you acquire this data?

Articles about the topic of terrorist attack as published on theguardian.com. Articles will be collected using the Guardian API. API enables to retrieve articles for different topics with keyword search. The keywords used to retrieve relevant articles will have to be identified (e.g. 'terrorism', 'terrorist atack', 'terrorist').

Articles will be stored in MongoDB collections.

If necessary, articles from other news organisation will be used as well, using relevant APIs.


## 4. In brief, outline your approach to solving this problem (knowing that this might change later).

1. Tokenizing and stemming each article
2. Calcuting term frequency using TF-IDF
3. Calcuting distance between different articles
4. Clustering articles using k-means, or similar
5. Potentially other steps to improve results of the clustering (e.g. LDA, WARD clustering)
6. Custom visualisation of the results


## 5. What are your deliverables? Typically, this would include code, along with a paper and/or a slide deck.

Fully documented source code for the text analysis, and a custom visualisation with the results of the clustering. Visualisation will be either explanatory or exploratory, depending on the results of the analysis phase. An examples of what the final visualisation are [Stereotropes](http://stereotropes.bocoup.com/) and [Arms Globe](https://armsglobe.chromeexperiments.com/).
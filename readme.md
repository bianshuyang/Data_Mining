**Project Report**: [https://github.com/bianshuyang/Data_Mining/blob/main/Project_Report.pdf](https://github.com/bianshuyang/Data_Mining/blob/main/Project_Report.pdf)


| Sprint # | Date       | Item             |Author            |
|----------|------------|------------------|------------------|
| 1        | 2024-02-01 |Gathering Data    |Simon, Nazif      |
| 2        | 2024-02-07 |GPA,GRE,program   |Tuan              |
| 3        | 2024-02-10 |Program Popularity|Nazif, Simon      |
| 4        | 2024-02-15 |Time Analysis     |Tuan              |
| 5        | 2024-02-20 |Predictive Model  |Tuan              |
| 6        | 2024-02-25 |Sentiment Analysis|Simon             |
| 7        | 2024-03-01 |Topic Modeling    |Simon             |
| 8        | 2024-03-06 |Scholarship       |Nazif             |
| 9        | 2024-03-11 |Geographical      |Simon             |
| 10       | 2024-03-16 |Recommendation Sys|Tuan              |
| 11       | 2024-03-21 |Clustering        |Simon, Nazif      |
| 12       | 2024-03-26 |Literature Review |Simon, Tuan       |
| 13       | 2024-04-02 |Math Imagination  |Tuan              |
| 14       | 2024-04-07 |Latex Format      |Nazif             |
| 15       | 2024-04-13 |Powerpoint Pres   |All               |
| 16       | 2024-04-19 |ProofReading      |All               |

**Product Backlog**
1. [ ] Clean the data. Handle the different degrees gracefully. Apply good norminalization on Date, GRE, and GPA. Uniform the programs and the universities.
2. [ ] Do a simple graph on: x axis = GPA, y axis = GRE ( through which methods we normalize these three sub scores?) , and a colormetric (red, orange, and green to represent accept, interview, or reject) as in niche.com
3. [ ] Use a Sankey graph (can use my code: [https://github.com/NLP-Suite/NLP-Suite/blob/current-stable/src/charts_util.py](https://github.com/NLP-Suite/NLP-Suite/blob/current-stable/src/charts_util.py)) and represent the rates of universities and students, using the bining methods to select categories: high GPA high GRE, high GPA low GRE, totaling up to 4 for two attributes, or 8 if we can extract publication from the data. Then do another Snakey graph suggesting on how major affects the results.
4. [ ] Do a geographic map on the region to which the students apply and a Sankey plot for each of the region. Use geopy or nominatim for extracting university locations.
5. [ ] Do a chronological analysis on the data. How do you view the response to be different, for varied major? Classify into humanities, allied health, CS, Traditional BioChemEnv, Engineerinng, etc. other bins, to observe for users' participation rates. Observe for simple metrics on the text. What do these text manifest over time? Use BERT to extract for sentiment information encoded in the data.
6. [ ] How could we use tree (see R: transaction model) for the categorization of students? Any existing Bayesian model for classification and a decision tree?
7. [ ] How does we use machine learning to predict the results of a student?
8. [ ] Observe for topics in the comments of students. How have some wodclouds, verbs, nouns, etc. other NLP metrics been changing? Observe for results.

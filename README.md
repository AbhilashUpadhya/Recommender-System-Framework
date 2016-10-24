# Recommender-System-Framework
A sophisticated Recommender System that provides recommendations to users on different datasets available like GroupLens, Amazon, Goodreads, Coursera, using a hybrid recommender system engine. The framework allows the user to configure their recommender system with different ML algorithms to achieve the best recommendations possible. To assist a variety of datasets, the framework also included a Data Source component. Finally, the framework included a Feedback loop component to better the efficiency of the recommendations.

# DASE ARCHITECTURE
The Dase architecture consistes of 4 components
Data Source (Which takes up different types of data sets and makes it ready for the engine)
Data preparator (Pre-Filtering algorithms to increase efficiency of the predictions: White list and black list can be created here)
Recommender Engine (A combination of different recommender system algorithms according for user to test: Training and Testing of datasesets)
Feedback Loop (Prediction accuracy is increased and the best combination of algorithms are decided for real time recommendations)

# Mongo DB
Scalable back-end DB with Mongo DB

=Algorithms Supported=
Collaborative Filtering Algorithm
Content-Based Filtering Algorithm - with item and/or user vectors 
Support Vector Machines
Bayesian classification Algorithm


# Data Analysis Using Python - Final Project
# IMDB 5000 Movie Dataset

![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/extra/imdb.jpg)

## The data is of IMDB 5000 Movie Dataset is in the CSV format and the name of the file is movie_metadata.csv which contains all the information regarding the entire aspect of a movie.


# Analysis Performed

# Analysis 1

 - What kind of movies are liked by the audience, critics and producers and whether or not there is an overlap.
    The below performed analysis is used to derive the conclusion.
 - IMBD top 250 based on Keywords
 - Top 250 highest grossing movies based on Keywords
 - Top 250 movies with the highest budget based on Keywords

 
 
       - IMBD top 250 based on Keywords
 ![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_1/TopIMDBMoviesKeyword.png)
 
       - Top 250 highest grossing movies based on Keywords
 ![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_1/TopGrossingMoviesKeyword.png)
 
       - Top 250 movies with the highest budget based on Keywords
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_1/TopHIghestBudgetKeyword.png)

       - Comparision between all the three plots
 
 ![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_1/Comparision.png)

# Inference of Analysis 1

 * From the analysis we come to the conclusion that **Nudity and sex** seems to be a good selling point for blockbusters and the producers know it too as it is equally common in big budget movies.
 * People like to go to watch movies to which they can relate to that is why sex, nudity and relationship are the top 3 keywords in the highest grossing movies and producers and cinema houses seems to know their audience as well.

# Analysis 2

 * Based on the data avialable from IMDB Dataset we find out the **Best Director** of all times by using **Facebook Like,IMDB Score and Average Revenue**

        - HeatMap of all the parameters
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_2/HeatMap.png)

        - Venn Diagram Comparision to find the best director 
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_2/BestDirector.png)        
        
# Inference of Analysis 2

 * Based on the analysis done by comparing all the facebook likes which shows how popular a director is among masses,How much successful he is in terms of revenue generated and imdb score which evolves with time we come to the conclusion that **Christopher Nolan** is the best director.

# Analysis 3

* Doing a **Comparative analysis** of how successful **horror movies** are in terms of earnings with reference to **other genres** by gathered data in IMDB from over a period of many years. 

         - IMDB Score of horror movies and all films over the years
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_3/YearWiseIMDBMean.png)  

         - Comparision of Hit percentage between horror films and other movies
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_3/Comparision.png)

# Inference of Analysis 3

 * Based on the above analysis we come to the conclusion that films made on **horror genres is more successful than any other genres**.
 * Interesting to see that **Horror films have more success** at the box office compared to all movies in the dataset. 
 * Which implies that horror genre is more bankable as it's probability of being a hit is more.

# Analysis 4

 * This analysis takes into consideration the budget and the gross income from the movie and deduces the profit.
 * Thus we come to the conclusion of **Top biggest hit and biggest flop**.
 
        - The top Flops movies from tha available data are plotted below
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_4/TopFlops.png)           
        
        - The top Hits movies from tha available data are plotted below
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_4/TopHits.png)        

# Inference of Analysis 4

  * Based on the above analysis we come to the conclusion that these were the **Top Flops and Hits of all time**.

# Analysis 5

  * Analysis to find out that whether there is any correlation between **high imdb rated movie** with it's **profit**.
  * Which genres got maximum >= 7 ratings
  * Which genres are most profitable
  
         - IMDB rating of all genres of movies having more than or equal to 7 rating
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_5/HighIMDBHenres.png)  
         
         
         - The profits of all genres of movies are specified below
![alt text](https://github.com/kunalmsharma/sharma_kunal_spring2017/blob/master/Final/analysis/ana_5/ProfitofGenres.png)  
# Inference of Analysis 5

 * As we can see **Drama,Comedy and Thriller** have maximum number of films in this category but if you look at it's profit it's not very much compared to other genres.
 * From the above analysis we can certainly say that genres with **more imdb score** need **not** be the most profitable genres to produce movies in.
 * As we can see that **imdb score is not directly proportional to box office collection**.

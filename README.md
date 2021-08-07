# Degree of Profanity for Racial Slurs

This is a small python program which tags a profanity degree ( "HIGH" or "LOW" ) based on the slur words present in a tweet/sentence.

## Project Tree:
```bash
|-- Data
|   |-- ethnic_slurs.csv
|-- tweets_data.csv
|-- output_result.csv
|-- profanity_degree.py
```

* ### profanity_degree.py :
  * This program takes an input file e.g tweets_data.csv
  * And using the profanityfilter library methods, it tags a profanity-degree of either "HIGH" or "LOW" to the tweets/sentences based on the presence of slur words.
  * The tagged tweets/sentence is next written in a output_result.csv file.


* ### Data : ethnic_slurs.csv
  * This is scraped dataset of ethnic slur terms from the wikipedia website : https://en.wikipedia.org/wiki/List_of_ethnic_slurs.
  * One can personalise the dataset by adding custom slur/other words collection.


### Credits
This project is built on the library [profanityfilter](https://github.com/areebbeigh/profanityfilter) by [@areebbeigh](https://github.com/areebbeigh)


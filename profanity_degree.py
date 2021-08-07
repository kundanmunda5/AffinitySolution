from csv import reader, writer                  # to operate on csv files
from os import error                            # to handle I/O errors       
from pathlib import Path                        # to manage Paths
from profanityfilter import ProfanityFilter     # to check the Profanity of words

# constants
CUSTOM_SLUR_WORD_FILE = './Data/racial_slur_collection/ethnic_slurs.csv'
OUTPUT_FILE = './output_result.csv'
INPUT_FILE = './Data/tweets_data.csv'
HEADER = ['ProfanityDegree','Twitter_ID','Tweet']


class Profanity:
    def __init__(self):
        self.pf = ProfanityFilter()
        self.fetched_tweets = []


    def add_words(self, file_path = None):
        # adds the custome slur words to the profanityfilter data set
        try:
            if(file_path != None):
                with open(file_path, 'r') as f:
                    custom_censor_list = [line.strip() for line in f.readlines()]
                    self.pf.append_words(custom_censor_list)
        except error:
            print("ERROR :: Couldn't find the path for custom slur words")
        

    def collect_tweets(self, tweet_file = None):
        # collects tweets from the given input tweet dataset
        try:
            if tweet_file != None:
                with open(Path(tweet_file), 'r') as read_obj:
                    csv_reader = reader(read_obj)

                    header = next(csv_reader)

                    if header != None:
                        self.check_profanity(csv_reader)
                        
        except error:
            print("ERROR :: check the path given for input tweet dataset file")

    
    def check_profanity(self, csv_reader = None):
        # checks the profanity of each word by matching it with profanityfilter dataset
        try:
            if csv_reader != None:
                for row in csv_reader:
                            profanity_degree = "HIGH" if self.pf.is_profane(row[1]) else "LOW"

                            self.fetched_tweets.append([profanity_degree, row[0], row[1]])

        except error:
            print("ERROR :: CHECK the instance reference given to the csv reader object")
    

    def write_output(self, processed_rows = []):
        # writes the output result to the file in the directed path
        try:
            if len(processed_rows):
                try:
                    with open(Path(OUTPUT_FILE), 'w+', newline='') as write_obj:
                        csv_writer = writer(write_obj)
                        csv_writer.writerow(HEADER)
                        csv_writer.writerows(processed_rows)
                except error:
                    print("ERROR :: failure in writing output to the destined file")

        
        except error:
            print("ERROR :: Problem with the processed fetched tweets")


def main(dataset):
    profanity = Profanity()

    # adding the custom slur words from the racial_slur_collection
    profanity.add_words(CUSTOM_SLUR_WORD_FILE)

    # calling function to read and fetch tweets from the input tweet dataset and process the data
    profanity.collect_tweets(dataset)

    # write the output file
    profanity.write_output(profanity.fetched_tweets)
     

if __name__ == '__main__':
    
    main(INPUT_FILE)

    print("-"*62+"\n\tPROCESSED THE tweets_data.csv SUCCESSFULLY\n\tCHECK THE 'output_result.csv' for RESULTS\n"+"-"*62)
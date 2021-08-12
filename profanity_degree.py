from csv import reader, writer                  # to operate on csv files

from pathlib import Path                        # to manage Paths
from profanityfilter import ProfanityFilter     # to check the Profanity of words
import sys,os                                   # to handle command line arguments and os errors

# constants
CUSTOM_SLUR_WORD_FILE = './twitter-profanity-check/Data/racial_slur_collection/ethnic_slurs.csv'
OUTPUT_FILE = './output_result.csv'
INPUT_FILE = './Data/tweets_data.csv'
HEADER = ['ProfanityDegree','Twitter_ID','Tweet']
# AffinitySolution\twitter-profanity-check\Data\racial_slur_collection\ethnic_slurs.csv
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
        except:
            print("ERROR :: Couldn't find the path for custom slur words",os.error)
        

    def collect_tweets(self, tweet_file = None):
        # collects tweets from the given input tweet dataset
        try:
            if tweet_file != None:
                with open(Path(tweet_file), 'r') as read_obj:
                    csv_reader = reader(read_obj)

                    header = next(csv_reader)

                    if header != None:
                        self.check_profanity(csv_reader)
                        
        except:
            print("ERROR :: check the path given for input tweet dataset file")

    
    def check_profanity(self, csv_reader = None):
        # checks the profanity of each word by matching it with profanityfilter dataset
        try:
            if csv_reader != None:
                for row in csv_reader:
                            profanity_degree = "HIGH" if self.pf.is_profane(row[1]) else "LOW"

                            self.fetched_tweets.append([profanity_degree, row[0], row[1]])

        except:
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
                except os.error:
                    print("ERROR :: failure in writing output to the destined file")

        
        except:
            print("ERROR :: Problem with the processed fetched tweets")


def main(dataset):
    profanity = Profanity()

    # to check command line path for data input
    try:
        if(dataset != None):
         INPUT_FILE = dataset
         print("input_file ",INPUT_FILE)
         
    except:
        print("ERROR :: please input correct path for the input file")

    # adding the custom slur words from the racial_slur_collection
    profanity.add_words(CUSTOM_SLUR_WORD_FILE)

    # calling function to read and fetch tweets from the input tweet dataset and process the data
    profanity.collect_tweets(dataset)

    # write the output file
    profanity.write_output(profanity.fetched_tweets)
     

if __name__ == '__main__':
    
    try:
        if(os.path.exists(sys.argv[1]) and len(sys.argv) == 2):
            arg_file_path = sys.argv[1]
            # print(os.path.basename(arg_file_path))
            print(os.path.exists(arg_file_path))
            # print(os.defpath(arg_file_path))
            # print(os.path.abspath(arg_file_path))

            main(Path(sys.argv[1]))
            

            print("-"*70+"\n\tPROCESSED THE tweets_data.csv SUCCESSFULLY\n\tCHECK THE 'output_result.csv' for RESULTS\n"+"-"*70)


        else:
            print("length of argv", len(sys.argv)) 
            print("-"*70+"\n\t\t\tUnable to process\n->CHECK THE 'PATH' of the relevant .csv file\n->for spaced folder or file names use '' e.g. '/folder name/file.csv'\n"+"-"*70)
    except:
        print("Problem :: exception in the in the main function")





#   FOR TESTING THE ARGUMENT INPUT VALUES
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
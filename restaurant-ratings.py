# your code goes here

scores_doc = open("scores.txt")

def format_restaurant_scores(file_name):
    """ """

    scores_for_restaurants = {}

    for line in file_name:
        line = line.rstrip()
        words = line.split(":")
        
        restaurants = words[0]
        scores = words[1]    
        
        for each_line in words:
            scores_for_restaurants[restaurants] = scores

        # final_scores = scores_for_restaurants.items()
            
            
    print scores_for_restaurants

format_restaurant_scores(scores_doc)    
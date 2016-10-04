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
        scores_for_restaurants[restaurants] = scores

     
    for restaurants, scores in scores_for_restaurants.items():
        print "%s is rated at %s" % (restaurants, scores)

format_restaurant_scores(scores_doc)


 
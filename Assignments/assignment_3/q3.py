def score(file):
    # READING IN THE NECESSARY FILES. DO NOT EDIT #
    # This is a list of lists, where each sublist is [word, score]
    # e.g. [["vile", "-3.18"], ["beautiful", "3.07"]]
    word_scores = read_sentiment("sent_scores.txt")

    # This is a list of words within the file
    data = read_review(file) 
    # DO NOT EDIT ABOVE
    ###############################################

    # WRITE YOUR ANSWER BELOW
    
    # Convert word_scores to a dictionary for easier lookup
    score_dict = {word.lower(): float(score) for word, score in word_scores}
    
    total_score = 0
    word_impacts = {}
    
    for word in data:
        # Convert word to lowercase and remove any non-alphanumeric characters
        clean_word = ''.join(char.lower() for char in word if char.isalnum())
        
        if clean_word in score_dict:
            score = score_dict[clean_word]
            total_score += score
            
            # Track the impact of each word
            if clean_word in word_impacts:
                word_impacts[clean_word] += abs(score)
            else:
                word_impacts[clean_word] = abs(score)
    
    # Find the most impactful word
    most_impactful = max(word_impacts, key=word_impacts.get) if word_impacts else ""
    
    return (round(total_score, 2), most_impactful)
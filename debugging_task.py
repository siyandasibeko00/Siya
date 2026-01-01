# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) #replaced k with key in square brackets

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", #replaced single quotation with double quotation
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) #placed square brackets to form list between lisa and homer

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
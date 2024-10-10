import re

def split_into_sub_sentences(text):
    """
    Splits the text into sub-sentences based on specific separators.
    
    Parameters:
    text (str): The input text to be split.
    
    Returns:
    list: A list of sub-sentences.
    """
    # Define separators to split the text
    separators = r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat "
    # Replace all separators with a marker "|"
    marked_text = re.sub(separators, "|", text)
    # Split the text on marker "|"
    sub_sentences = marked_text.split("|")
    return sub_sentences

def calculate_ego_score(sub_sentences):
    """
    Calculates the ego score based on the list of sub-sentences.
    
    Parameters:
    sub_sentences (list): A list of sub-sentences.
    
    Returns:
    int: The ego score.
    """
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.strip().lower()  # Clean up the sentence
        if sentence:
            words = sentence.split()  # Split sentence into words
            # Check if the first or second word is 'ik' or 'mijn'
            if any(word in ('ik', 'mijn') for word in words[:2]):
                ego_score += 1
    return ego_score

# Test the functions with different texts
text = """Geachte heer/mevrouw,
Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. Ik ben buitengewoon slim en in staat om snel nieuwe informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf. Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf, en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. Ik verdien daarom een plek in uw team.
Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen, zodat ik u persoonlijk kan overtuigen van mijn geschiktheid voor deze functie."""

sub_sentences = split_into_sub_sentences(text)
ego_score = calculate_ego_score(sub_sentences)
print(f"Ego Score: {ego_score}")
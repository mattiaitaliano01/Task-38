import spacy

def watch_next(description):
    nlp = spacy.load('en_core_web_md')
    doc = nlp(description)
    with open ("movies.txt", "r") as file:
        similarity = 0
        for line in file:
            movie_description = nlp(line.split(":")[1])
            if doc.similarity(movie_description) > similarity:
                similarity = doc.similarity(movie_description)
                next_film = line.split(":")[0]
        print(next_film)

title = "Hulk"

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

watch_next(description)

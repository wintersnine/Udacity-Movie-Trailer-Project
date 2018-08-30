import media
# import of media file that contains classes, constructors, and instance methods
import fresh_tomatoes
# import file required to generate movie website

thor_ragnarok = media.Movie("Thor: Ragnarok",
                    "Thor is imprisoned and tries to save his world and civilization",
                    # this is the movie storyline of Thor: Ragnarok
                    "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                    # movie poster of Thor: Ragnarok                           
                    "https://www.youtube.com/watch?v=v7MGUNV8MxU")
                    # trailer of Thor: Ragnarok  

moana = media.Movie("Moana",
                    "Moan sets sail to find Maui, on a quest to help save her people",
                    # this is the movie storyline of Moana
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                    # movie poster of Moana                            
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")
                    # trailer of Moana      
                    
rio_2 = media.Movie("Rio 2",
                    "Two Blue macaws take their childrento to visit their family.",
                    # this is the movie storyline of Rio 2
                    "https://upload.wikimedia.org/wikipedia/en/6/67/Rio_2_Poster.JPG",
                    # movie poster of Rio 2                         
                    "https://www.youtube.com/watch?v=leJuOObuCxM")
                    # trailer of Rio 2

the_secret_life_of_walter_mitty = media.Movie("The Secret Life of Walter Mitty",
                    "A search for the missing photo for a magazine's final print.",
                    # this is the movie storyline of The Secret Life of Walter Mitty
                    ("https://upload.wikimedia.org/wikipedia/en/c/cd/"
                    "The_Secret_Life_of_Walter_Mitty_poster.jpg"),
                    # movie poster of The Secret Life of Walter Mitty                          
                    "https://www.youtube.com/watch?v=QD6cy4PBQPI")
                    # trailer of The Secret Life of Walter Mitty

the_secret_life_of_pets = media.Movie("The Secret Life of Pets",
                    "Pets struggling to find their way back home",
                    # this is the movie storyline of The Secret Life of Pets
                    ("https://upload.wikimedia.org/wikipedia/en/6/64/"
                    "The_Secret_Life_of_Pets_poster.jpg"),
                    # movie poster of The Secret Life of Pets                         
                    "https://www.youtube.com/watch?v=i-80SGWfEjM")
                    # trailer of The Secret Life of Pets

guardians_of_the_galaxy_vol_2 = media.Movie("Guardians of the Galaxy Vol 2",
                    "Starlord finds out about his dad, and the troubles that come with it",
                    # this is the movie storyline of Guardians of the Glaxy Vol 2
                    ("https://upload.wikimedia.org/wikipedia/en/a/ab/"
                    "Guardians_of_the_Galaxy_Vol_2_poster.jpg"),
                    # movie poster of Guardians of the Galaxy Vol 2                          
                    "https://www.youtube.com/watch?v=dW1BIid8Osg")
                    # trailer of Guardians of the Galaxy Vol 2

# list of movies
movies = [thor_ragnarok, moana, rio_2, the_secret_life_of_walter_mitty,
          the_secret_life_of_pets, guardians_of_the_galaxy_vol_2]
fresh_tomatoes.open_movies_page(movies)

import fresh_tomatoes
import movie


''' Here we defining an instances, group them into a list and open a page'''
# Movie 1
movies = []
title = "The Intouchables"
storyline = "An unlikely friendship develops between a wealthy quadriplegic and his caretaker."
image = "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg"
trailer = "https://www.youtube.com/watch?v=34WIbmXkewU"

movies.append(movie.Movie(title, storyline, image, trailer))

# Movie 2
title = "Yes Man"
storyline = 'He promised to answer "Yes!" to every opportunity, request, or invitation that presents itself.'
image = "https://upload.wikimedia.org/wikipedia/en/7/71/YesMan2008poster.jpg"
trailer = "https://www.youtube.com/watch?v=M3ar1tBj_Zk"

movies.append(movie.Movie(title, storyline, image, trailer))

# Movie 3
title = "The Shawshank Redemption"
storyline = 'He was found guilty and sentenced to serve two life sentences back to back at Shawshank Prison.'
image = "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg"
trailer = "https://www.youtube.com/watch?v=K_tLp7T6U1c"

movies.append(movie.Movie(title, storyline, image, trailer))

# Movie 4
title = "Some Like it Hot"
storyline = 'Two musicians who dress in drag in order to escape from mafia gangsters.'
image = "https://upload.wikimedia.org/wikipedia/en/b/b4/Some_Like_It_Hot_poster.jpg"
trailer = "https://www.youtube.com/watch?v=rI_lUHOCcbc"

movies.append(movie.Movie(title, storyline, image, trailer))

# Movie 5
title = "Pulp Fiction"
storyline = 'Storylines of Los Angeles mobsters, fringe players, small-time criminals, and a mysterious briefcase'
image = "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg"
trailer = "https://www.youtube.com/watch?v=WSLMN6g_Od4"

movies.append(movie.Movie(title, storyline, image, trailer))

# Movie 6
title = "How to Steal a Million"
storyline = 'Is it possible to steal the Venus?'
image = "https://upload.wikimedia.org/wikipedia/en/8/8a/Howtostealamillion.jpg"
trailer = "https://www.youtube.com/watch?v=ri4KsE2lvpw"

# group all the Movie instances together in a list.
movies.append(movie.Movie(title, storyline, image, trailer))

# open a page
fresh_tomatoes.open_movies_page(movies)

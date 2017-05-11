# moviedownload
Controller.py - Gets all the movie title from the home page yts.ag using beautifulsoup. User has to select the movie's index number. moviedown.py will then get called with additional command line argument (movie name).

moviedown.py- Gets json information about the given movie from omdbapi.com. It then contructs the movie's url (yts.ag/movie-url-here) and then scraps the page for magnet links using beautifulsoup. It then calles the system to open the magnet link found.

import unittest
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):

    # media_one = proj1.Media()
    # media_two = proj1.Media("1999", "Prince", "1982")
    #
    # song_one = proj1.Song()
    # song_two = proj1.Song("6 Inch", "Beyonce", "2016", "Lemonade", 260000, "R&B")
    #
    # movie_one = proj1.Movie()
    # movie_two = proj1.Movie("Pan's Labyrinth", "Guillermo del Toro", "2006", "R", 7105000)

    def testConstructor(self):

        media_one = proj1.Media()
        media_two = proj1.Media("1999", "Prince", "1982")

        self.assertEqual(media_one.title, "No Title")
        self.assertEqual(media_one.author, "No Author")
        self.assertEqual(media_one.release_year, "No Release Year")
        self.assertEqual(media_two.title, "1999")
        self.assertEqual(media_two.author, "Prince")
        self.assertEqual(media_two.release_year, "1982")

        song_one = proj1.Song()
        song_two = proj1.Song("6 Inch", "Beyonce", "2016", "Lemonade", 260000, "R&B")

        self.assertEqual(song_one.album, "No Album name")
        self.assertEqual(song_one.track_length, "No Track Length")
        self.assertEqual(song_two.album, "Lemonade")
        self.assertEqual(song_two.track_length, 260000)

        movie_one = proj1.Movie()
        movie_two = proj1.Movie("Pan's Labyrinth", "Guillermo del Toro", "2006", "R", 7115000)

        self.assertEqual(movie_one.rating, "No Rating")
        self.assertEqual(movie_one.movie_length, "No Movie Length")
        self.assertEqual(movie_two.rating, "R")
        self.assertEqual(movie_two.movie_length, 7115000)

    def testStringMethods(self):

        media_one = proj1.Media()
        media_two = proj1.Media("1999", "Prince", "1982")
        song_one = proj1.Song()
        song_two = proj1.Song("6 Inch", "Beyonce", "2016", "Lemonade", 260000, "R&B")
        movie_one = proj1.Movie()
        movie_two = proj1.Movie("Pan's Labyrinth", "Guillermo del Toro", "2006", "R", 7115000)

        self.assertEqual(media_one.__str__(), "No Title by No Author (No Release Year)")
        self.assertEqual(media_two.__str__(), "1999 by Prince (1982)")
        self.assertEqual(song_one.__str__(), "No Title by No Author (No Release Year) [No Genre]")
        self.assertEqual(song_two.__str__(), "6 Inch by Beyonce (2016) [R&B]")
        self.assertEqual(movie_one.__str__(), "No Title by No Author (No Release Year) [No Rating]")
        self.assertEqual(movie_two.__str__(), "Pan's Labyrinth by Guillermo del Toro (2006) [R]")

    def testLenMethods(self):

        media_one = proj1.Media()
        media_two = proj1.Media("1999", "Prince", "1982")
        song_one = proj1.Song()
        song_two = proj1.Song("6 Inch", "Beyonce", "2016", "Lemonade", 260000, "R&B")
        movie_one = proj1.Movie()
        movie_two = proj1.Movie("Pan's Labyrinth", "Guillermo del Toro", "2006", "R", 7115000)

        self.assertEqual(media_two.__len__(), 0)
        self.assertEqual(song_one.__len__(), "No Track Length")
        self.assertEqual(song_two.__len__(), 260)
    #    self.assertEqual(len(song_two), 260)
        self.assertEqual(movie_one.__len__(), "No Movie Length")
        self.assertEqual(movie_two.__len__(), 119)

unittest.main()

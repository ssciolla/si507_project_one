import unittest
import json
import proj1_w18 as proj1

def create_test_cases():
    media_one = proj1.Media()
    media_two = proj1.Media("1999", "Prince", "1982")
    song_one = proj1.Song()
    song_two = proj1.Song("6 Inch", "Beyonce", "2016", "Lemonade", 260000, "R&B")
    movie_one = proj1.Movie()
    movie_two = proj1.Movie("Pan's Labyrinth", "Guillermo del Toro", "2006", "R", 7105000)
    test_cases_part_one = [media_one, media_two, song_one, song_two, movie_one, movie_two]
    return test_cases_part_one

def fetch_sample_json():
    file_open = open("sample_json.json", "r")
    list = json.loads(file_open.read())
    file_open.close()
    return list

def check_results(list):
    for item in list:
        if item != "All Good":
            return False
    return True

def test_if_correct_vars(class_instance):
    if isinstance(class_instance, proj1.Song):
        results = []
        results.append(getattr(class_instance, "movie_length", "All Good"))
        results.append(getattr(class_instance, "rating", "All Good"))
        return check_results(results)
    elif isinstance(class_instance, proj1.Movie):
        results = []
        results.append(getattr(class_instance, "track_length", "All Good"))
        results.append(getattr(class_instance, "album", "All Good"))
        results.append(getattr(class_instance, "genre", "All Good"))
        return check_results(results)
    elif isinstance(class_instance, proj1.Media):
        results = []
        results.append(getattr(class_instance, "track_length", "All Good"))
        results.append(getattr(class_instance, "album", "All Good"))
        results.append(getattr(class_instance, "genre", "All Good"))
        results.append(getattr(class_instance, "movie_length", "All Good"))
        results.append(getattr(class_instance, "rating", "All Good"))
        return check_results(results)

class TestMedia(unittest.TestCase):

    def testConstructor(self):
        # Testing Media instances
        self.assertEqual(create_test_cases()[0].title, "No Title")
        self.assertEqual(create_test_cases()[0].author, "No Author")
        self.assertEqual(create_test_cases()[0].release_year, "No Release Year")
        self.assertEqual(create_test_cases()[1].title, "1999")
        self.assertEqual(create_test_cases()[1].author, "Prince")
        self.assertEqual(create_test_cases()[1].release_year, "1982")
        self.assertTrue(test_if_correct_vars(create_test_cases()[1]))

        # Testing Song instances
        self.assertEqual(create_test_cases()[2].album, "No Album name")
        self.assertEqual(create_test_cases()[2].track_length, "No Track Length")
        self.assertEqual(create_test_cases()[3].album, "Lemonade")
        self.assertEqual(create_test_cases()[3].track_length, 260000)
        self.assertTrue(test_if_correct_vars(create_test_cases()[3]))

        # Testing Movie instances
        self.assertEqual(create_test_cases()[4].rating, "No Rating")
        self.assertEqual(create_test_cases()[4].movie_length, "No Movie Length")
        self.assertEqual(create_test_cases()[5].rating, "R")
        self.assertEqual(create_test_cases()[5].movie_length, 7105000)
        self.assertTrue(test_if_correct_vars(create_test_cases()[5]))

    def testStringMethods(self):
        self.assertEqual(create_test_cases()[0].__str__(), "No Title by No Author (No Release Year)")
        self.assertEqual(create_test_cases()[1].__str__(), "1999 by Prince (1982)")
        self.assertEqual(create_test_cases()[2].__str__(), "No Title by No Author (No Release Year) [No Genre]")
        self.assertEqual(create_test_cases()[3].__str__(), "6 Inch by Beyonce (2016) [R&B]")
        self.assertEqual(create_test_cases()[4].__str__(), "No Title by No Author (No Release Year) [No Rating]")
        self.assertEqual(create_test_cases()[5].__str__(), "Pan's Labyrinth by Guillermo del Toro (2006) [R]")

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

    def testMediaJSON(self):
        bridget_jones = proj1.Media(json=fetch_sample_json()[2])
        print(bridget_jones)
        self.assertEqual(bridget_jones.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(bridget_jones.author, "Helen Fielding")
        self.assertEqual(bridget_jones.release_year, "2012")
        self.assertEqual(bridget_jones.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(bridget_jones.__len__(), 0)

    def testTrackJSON(self):
        hey_jude = proj1.Song(json=fetch_sample_json()[1])
        print(hey_jude)
        self.assertEqual(hey_jude.title, "Hey Jude")
        self.assertEqual(hey_jude.author, "The Beatles")
        self.assertEqual(hey_jude.release_year, "1968")
        self.assertEqual(hey_jude.album, "TheBeatles 1967-1970 (The Blue Album)")
        self.assertEqual(hey_jude.track_length, 431333)
        self.assertEqual(hey_jude.genre, "Rock")
        self.assertEqual(hey_jude.__str__(), "Hey Jude by The Beatles (1968) [Rock]")
        self.assertEqual(hey_jude.__len__(), 431.333)

    def testMovieJSON(self):
        jaws = proj1.Movie(json=fetch_sample_json()[0])
        print(jaws) # Why is this getting printed second?
        self.assertEqual(jaws.title, "Jaws")
        self.assertEqual(jaws.author, "Steven Spielberg")
        self.assertEqual(jaws.release_year, "1975")
        self.assertEqual(jaws.rating, "PG")
        self.assertEqual(jaws.movie_length, 7451455)
        self.assertEqual(jaws.__str__(), "Jaws by Steven Spielberg (1975) [PG]")
        self.assertEqual(jaws.__len__(), 124)

unittest.main()

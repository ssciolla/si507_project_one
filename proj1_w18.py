import json

class Media:

	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", json=None):
		if json == None:
			self.title = title
			self.author = author
			self.release_year = release_year
		else:
			if "trackName" in json.keys():
				self.title = json["trackName"]
			else:
				self.title = json["collectionName"]
			self.author = json["artistName"]
			self.release_year = json["releaseDate"][:4]

	def __str__(self):
		string_rep = "{} by {} ({})".format(self.title, self.author, self.release_year)
		return string_rep

	def __len__(self):
		return 0

class Song(Media):

	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", album="No Album name", track_length="No Track Length", genre="No Genre", json=None):
		super().__init__(title, author, release_year, json)
		if json == None:
			self.album = album
			self.track_length = track_length
			self.genre = genre # Assignment doesn't say to do this, but otherwise, I'd have to input it again in the __str__ method.
		else:
			self.album = json["collectionName"]
			self.track_length = json["trackTimeMillis"]
			self.genre = json["primaryGenreName"]

	def __str__(self):
		base_rep = super().__str__()
		string_rep = base_rep + " [{}]".format(self.genre)
		return string_rep

	def __len__(self): # Return to this later; if statement may need to be changed
		if self.track_length == "No Track Length":
			return self.track_length
		else:
			time_in_sec = self.track_length / 1000
			return time_in_sec

class Movie(Media):

	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", rating="No Rating", movie_length="No Movie Length", json=None):
		super().__init__(title, author, release_year, json)
		if json == None:
			self.rating = rating
			self.movie_length = movie_length
		else:
			self.rating = json["contentAdvisoryRating"]
			self.movie_length = json["trackTimeMillis"]

	def __str__(self):
		base_rep = super().__str__()
		string_rep = base_rep + " [{}]".format(self.rating)
		return string_rep

	def __len__(self): # Return to this later; if statement may need to be changed
		if self.movie_length == "No Movie Length":
			return self.movie_length
		else:
			time_in_sec = self.movie_length / 1000
			time_in_min = time_in_sec // 60
			if time_in_sec % 60 >= 30:
				time_in_min += 1
			return time_in_min

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass

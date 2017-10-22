class Movie:
    def __init__(self, title, movie_genre_ids, favorite_genres):
        self.title = title
        self.genre_ids = movie_genre_ids
        self.favorite_genres = favorite_genres
        self.score = self.compute_score

    def compute_score(self):
        score = 0
        number_of_genres = len(self.genre_ids)
        for i in range(0,16):
            if self.favorite_genres[i][2] in self.genre_ids:
                score += self.favorite_genres[i][1]
        score /= number_of_genres
        return score

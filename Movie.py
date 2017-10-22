class Movie:
    def __init__(self, movie_title, movie_genre_ids, favorite_genres):
        self.title = movie_title
        self.genre_ids = movie_genre_ids
        self.user_genres = favorite_genres
        self.score = self.compute_score

    def compute_score(self):
        score = 0
        number_of_genres = len(self.genre_ids)
        for i in range(0,16):
            if self.user_genres[i][2] in self.genre_ids:
                score += self.user_genres[i][1]
        score /= number_of_genres
        return score

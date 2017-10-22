class movie:
    popularity = 0
    top_three_genre_ids = list()
    def __init__(self, movie_title, movie_genre_ids, favorite_genres, popularity):
        self.title = movie_title
        self.genre_ids = movie_genre_ids
        self.user_genres = favorite_genres
        self.top_three_genre_ids = [favorite_genres[0], favorite_genres[1], favorite_genres[2]]
        self.popularity = popularity
        self.score = self.compute_score()

    def compute_score(self):
        score = 1
        number_of_genres = 0
        for i in range(0,16):
            if self.user_genres[i][2] in self.genre_ids:
                score *= (10*self.user_genres[i][1])
                number_of_genres += 1
                print(self.user_genres)
                print(self.top_three_genre_ids)
                if self.user_genres[i][2] in self.top_three_genre_ids:
                    score *= 10
        score /= number_of_genres
        return score + self.popularity

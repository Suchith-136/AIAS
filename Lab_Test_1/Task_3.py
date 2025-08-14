def recommend_movies():
    # List of movies with their genres
    movies = [
        {"title": "The Notebook", "genre": "love"},
        {"title": "Titanic", "genre": "love"},
        {"title": "La La Land", "genre": "love"},
        {"title": "Inception", "genre": "sci-fi"},
        {"title": "Interstellar", "genre": "sci-fi"},
        {"title": "The Matrix", "genre": "sci-fi"},
        {"title": "The Godfather", "genre": "crime"},
        {"title": "Pulp Fiction", "genre": "crime"},
        {"title": "The Dark Knight", "genre": "action"},
        {"title": "Mad Max: Fury Road", "genre": "action"},
        {"title": "John Wick", "genre": "action"},
        {"title": "Finding Nemo", "genre": "animation"},
        {"title": "Toy Story", "genre": "animation"},
        {"title": "Coco", "genre": "animation"},
        {"title": "The Conjuring", "genre": "horror"},
        {"title": "Get Out", "genre": "horror"},
        {"title": "A Quiet Place", "genre": "horror"},
        {"title": "Forrest Gump", "genre": "drama"},
        {"title": "The Shawshank Redemption", "genre": "drama"},
        {"title": "Fight Club", "genre": "drama"},
    ]

    # Get all unique genres
    genres = set(movie["genre"] for movie in movies)

    # Take user input for preferred genre
    user_genre = input("Enter your favourite genre: ").strip().lower()

    # Filter movies by user's preferred genre
    recommended = [movie["title"] for movie in movies if movie["genre"] == user_genre]

    if recommended:
        print("These are movies available:")
        for title in recommended[:3]:
            print(title)
    else:
        print(f"Sorry, no movies found for the genre '{user_genre}'.")
        print("Available genres are:")
        for genre in sorted(genres):
            print(genre)

# Allow the user to enter the input and get recommendations
if __name__ == "__main__":
    recommend_movies()


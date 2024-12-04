"""
Python Practice Exercise: Movie Collection Manager
Objective:
Create a Python program that manages a movie collection using various Python concepts. The program should allow users to:

1. Add movies to the collection.
2. Search for movies by specific criteria.
3. Display all movies in the collection.
4. Handle errors gracefully (e.g., invalid input, missing data).
5. Use object-oriented programming to structure the solution.

Exercise Instructions:

Define a Movie class:
Attributes: title (str), director (str), year (int), rating (float).
Include a method to display a movie's details (__str__ method).

Define a MovieCollection class:
Use a list to store movies.
Methods:
add_movie: Adds a new movie to the collection (accepts args or kwargs).
find_movies: Accepts a keyword argument to filter movies by title, director, or year. Returns matching movies.
display_all_movies: Displays all movies in the collection or a message if the collection is empty.

Error Handling:
Ensure users provide valid input types (e.g., year is an integer, rating is a float).
Handle scenarios where no movies match the search criteria.

Main Functionality:
Implement a main function where users can interact with the movie collection using a menu:

Add a movie.
Search for movies.
Display all movies.
Exit.

Type Hinting:
Use type hints for all function parameters and return types.
"""
from matplotlib.pyplot import title


class Movie:
    def __init__(self, title: str, director: str, year: int, rating: float):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def __str__(self) -> str:
        return f"The movie {self.title}, was directed by {self.director} in {self.year} with a rating of {self.rating}"

# Step 3: Implement the main function

class MovieCollection(Movie):
    def __init__(self):
        self.movies = []

    def add_movie(self, title:str, director:str, year:int, rating:float):
        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")
        if not isinstance(rating, (float, int)) or not (0 <= rating <= 5):
            raise ValueError("Rating must be a float or integer between 0 and 5.")
        movie = Movie(title, director, year, float(rating))
        self.movies.append(movie)
        print(f"Movie {title} added successfully!")

    def find_movies(self, **kwargs):
        if not kwargs:
            print("No search criteria provided.")
            return []

        key, value = next(iter(kwargs.items()))
        key = key.lower()
        filtered_movies = []

        for movie in self.movies:
            if key == "title" and value.lower() in movie.title.lower():
                filtered_movies.append(movie)
            elif key == "director" and value.lower() in movie.director.lower():
                filtered_movies.append(movie)
            elif key == "year" and isinstance(value, int) and movie.year == value:
                filtered_movies.append(movie)

        if not filtered_movies:
            print(f"No movies found matching {key} = '{value}'.")
        return filtered_movies


    def display_movies(self):
        if not self.movies:
            print("No movies in the collection.")
        else:
            for movie in self.movies:
                print(movie)


def main() -> None:
    collection = MovieCollection()
    while True:
        print("\nMovie Collection Manager")
        print("1. Add a movie")
        print("2. Search for movies")
        print("3. Display all movies")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                name = input("Enter the title: ")
                director = input("Enter the director: ")
                year = int(input("Enter the year: "))
                rating = float(input("Enter the rating: "))
                collection.add_movie(name, director, year, rating)
            elif choice == 2:
                search_key = input("Search by title, director, or year: ").strip().lower()
                search_value = input("Enter the value to search for: ").strip()
                if search_key == "year":
                    search_value = int(search_value)
                results = collection.find_movies(**{search_key: search_value})
                if results:
                    print("\nMatching movies:")
                    for movie in results:
                        print(movie)
            elif choice == 3:
                print("\nAll Movies in the Collection:")
                collection.display_movies()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                raise ValueError("Invalid choice, please try again.")
        except ValueError:
            print("Error: Please enter a valid choice.")


if __name__ == "__main__":
    main()

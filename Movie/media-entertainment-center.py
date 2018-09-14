import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",120, "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450&quality=8",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",120, "A marine on an alien planet",
                     "https://resizing.flixster.com/Yq4pN3qojAZDF6QJFd_yE2Zmr1o=/206x305/v1.bTsxMTE3Njc5MjtqOzE3ODU5OzEyMDA7ODAwOzEyMDA",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
interstellar = media.Movie("Interstellar", 120,
                            "A story about astronauts who are looking for new planet for thae makind to live on",
                            "https://img1.od-cdn.com/ImageType-400/0111-1/D58/E97/25/%7BD58E9725-930E-4E14-9ECD-51BCE0EC59CB%7DImg400.jpg",
                            "https://www.youtube.com/watch?v=zSWdZVtXT7E")

movies = [toy_story,avatar,interstellar]
fresh_tomatoes.open_movies_page(movies)
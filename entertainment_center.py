import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://brainsnorts.files.wordpress.com/2012/11/toy-story-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://c1.staticflickr.com/3/2495/4211101808_959e2a1601.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

#print(avatar.storyline)
#avatar.show_trailer()

sound_of_music = media.Movie("Sound of Music",
                             "Naval captain with seven children fell in love with tomboyish postulant",
                             "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
                             "https://www.youtube.com/watch?v=AwzAuCg-qiU")

#print(sound_of_music.storyline)
#sound_of_music.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "https://i.ytimg.com/vi/xlrwgT_0JBo/hqdefault_live.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


ratatouille = media.Movie("Ratatouille", "StoryLine",
                          "https://1.bp.blogspot.com/_OO7WbmARD08/SLAc1s0cEQI/AAAAAAAAIBE/71vOv8RvklM/s400/ratatouille+attr.jpg",
                          "https://www.youtube.com/watch?v=PTNP4-nIVo4")


hunger_games = media.Movie("Hunger Games", "Storyline",
                          "http://i.vimeocdn.com/video/561257648_1280x720.jpg",
                          "https://www.youtube.com/watch?v=MkvUNfySGQU")

#hunger_games.show_trailer()

movies = [toy_story, avatar, sound_of_music, school_of_rock, ratatouille, hunger_games]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)

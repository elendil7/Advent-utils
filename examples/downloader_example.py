from src import Api  # src is where all the files are currently located

# replace sessionid with your own session id
# this can be found by going to any AOC input
# going to f12 -> Storage -> Cookies
dl = Api("SESSION-ID")

# this will get the dataset for the year 2021 day 1
dl.get_data(2021, 1)

# submits the answer to 2021 day 1 level 2
dl.submit(2021, 1, 2, "answer")

# submits the answer to level 1 of the current day
dl.submit_today_level1("answer")

# submits the answer to level 2 of the current day
dl.submit_today_level2("answer")

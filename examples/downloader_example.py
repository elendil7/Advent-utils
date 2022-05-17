from src import Api  # src is where all the files are currently located

# replace sessionid with your own session id
# this can be found by going to any AOC input
# going to f12 -> Storage -> Cookies
dl = Api("SESSION-ID")

# this will get the dataset for the year 2021 day 1
dl.get_data(2021, 1)

# submits the answer to 2021 day 1 level 2
dl.submit(2021, 1, 2, "answer")

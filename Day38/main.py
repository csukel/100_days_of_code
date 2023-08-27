import requests
import datetime as dt
import pandas
NUTRITION_API_KEY = "591e7d2b48951359b8b0aee05a5b5f37"
NUTRITION_APP_ID = "7913d9e4"

EXCERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
DATA_PATH = "Day38/data.csv"
headers = {
	"x-app-id" : NUTRITION_APP_ID,
	"x-app-key" : NUTRITION_API_KEY,
	"Content-Type" : "application/json"
}

req_body = {
	"query" : input("Tell me which exercise you did: ")
}

res = requests.post(url=EXCERCISE_ENDPOINT, headers=headers, json=req_body)
res.raise_for_status()
exercises = res.json()["exercises"]

now = dt.datetime.now()

def get_time(time : dt.datetime, i):
	for exercise in exercises[:i]:
		time = time + dt.timedelta(seconds=exercise['duration_min'] * 60)
	return time.strftime("%H:%M:%S")

exercises_formatted = [
        {
			"Date" : now.strftime("%d/%m/%Y"),
			# "Time" : now.strftime("%H:%M:%S"),
			"Time" : get_time(now, i),
            "Exercise": exercise["name"],
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"],
        }
        for i, exercise in enumerate(exercises)
    ]

df_original = pandas.read_csv(DATA_PATH)

df = pandas.DataFrame(exercises_formatted)

df = pandas.concat([df_original, df])

df.to_csv(DATA_PATH, index=False)
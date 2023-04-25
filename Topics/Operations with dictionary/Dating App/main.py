def select_dates(potential_dates, age=30, location="Berlin", hobby="art"):
    return ", ".join([people.get("name") for people in potential_dates if
                      all([people.get("age") > age,
                           hobby in people.get("hobbies"),
                           people.get("city") == location])])

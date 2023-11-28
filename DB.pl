dob(john, date(1990, 5, 15)).
dob(lisa, date(1985, 10, 20)).
dob(mary, date(1995, 2, 8)).
dob(david, date(1980, 7, 3)).

get_dob(Person, Date) :-dob(Person, Date).


born_after(Year, Person) :-dob(Person, date(Year2, _, _)),Year2 > Year.
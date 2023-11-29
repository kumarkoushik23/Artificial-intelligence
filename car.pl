owns(jack, car(bmw)).
owns(john, car(chevy)).
owns(olivia, car(civic)).
owns(jane, car(chevy)).

% Car types
sedan(car(bmw)).
sedan(car(civic)).
truck(car(chevy)).


has_sedan(X) :-
    owns(X, car(Y)),
    sedan(car(Y)).


has_truck(X) :-
    owns(X, car(Y)),
    truck(car(Y)).
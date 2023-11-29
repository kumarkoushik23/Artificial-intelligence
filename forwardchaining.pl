ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(mary, pat).
parent(pat, jim).


generate_ancestors :-
    ancestor(X, Y),
    assert(ancestor(X, Y)),
    fail.
generate_ancestors.


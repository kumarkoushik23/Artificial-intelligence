fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(pear, green).

color_of(Fruit, Color) :-
    fruit_color(Fruit, Color).

fruits_of_color(Color, Fruits) :-
    setof(Fruit, color_of(Fruit, Color), Fruits).

colors_of_fruit(Fruit, Colors) :-
    setof(Color, color_of(Fruit, Color), Colors).
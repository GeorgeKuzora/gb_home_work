sumList([], 0).
sumList([H|T], Sum) :-
    sumList(T, SumT),
    Sum is H + SumT.

% query
sumList([1,2,3,4,5], Sum).

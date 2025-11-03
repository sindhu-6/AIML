from sympy import symbols,Or,Not,Implies,Xor,satisfiable

Rain=symbols('Rain')
Harry_visited_Hagrid=symbols('Harry_visited_Hagrid')
Harry_visited_Dumbledore=symbols('Harry_visited_Dumbledore')

sentence_1=Implies(Not(Rain),Harry_visited_Hagrid)
sentence_2=Xor(Harry_visited_Hagrid,Harry_visited_Dumbledore)
sentence_3=Harry_visited_Dumbledore

knowledge_base=sentence_1 & sentence_2 & sentence_3
solution=satisfiable(knowledge_base,all_models=True)
for model in solution:
    if model[Rain]:
        print("It rained today")
    else:
        print("There is no rain today")

turmas = [
     {'ações comunitárias', 'futebol', 'música', 'rugby'},
     {'ações comunitárias', 'música', 'rugby', 'teatro'},
     {'música', 'rugby', 'teatro', 'vôlei'},
     {'música', 'vôlei', 'rugby'},
     {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},
     {'ações comunitárias', 'futebol', 'rugby'},
     {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
     {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
     {'ações comunitárias', 'rugby', 'vôlei'}
]


atividades_comum = set(turmas[0]) 
for turma in turmas[1:]:
    atividades_comum &= turma 

print(atividades_comum)

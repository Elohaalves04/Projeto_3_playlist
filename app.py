import streamlit as st

generos = {
    'Internacional': {
        'Bruno Mars': 'https://www.youtube.com/watch?v=ekzHIouo8Q4',
        'Olivia Rodrigo': 'https://www.youtube.com/watch?v=cii6ruuycQA',
        'Adele': 'https://www.youtube.com/watch?v=BW9Fzwuf43c',
        'Joe Keery': 'https://www.youtube.com/watch?v=Ec08db2hP10'
    },
    'Sertanejo': {
        'Luan Santana': 'https://www.youtube.com/watch?v=36W_wRuPYbs',
        'Jorge e Mateus': 'https://www.youtube.com/watch?v=ICS6uKC93w0',
        'Matheus e Kauan': 'https://www.youtube.com/watch?v=8Hm3WkmS16M',
        'Marilia Mendonça': 'https://www.youtube.com/watch?v=wje4zcGgSqA'
    },
    'MPB': {
        'Tribalistas': 'https://www.youtube.com/watch?v=3JiMr-HgHJ8',
        'Chico Buarque': 'https://www.youtube.com/watch?v=bGAJlOwUgHY',
        'Caetano Veloso': 'https://www.youtube.com/watch?v=j9UbE1slI-Q',
        'Marisa Monte': 'https://www.youtube.com/watch?v=BM-mnklMWCQ'
    },
    'Pagode' : {
        'Ferrugem': 'https://www.youtube.com/watch?v=o3dknP3jclw',
        'Pericles': 'https://www.youtube.com/watch?v=AENA_nvF-L0',
        'Arlindo Cruz': 'https://www.youtube.com/watch?v=-HAbOWi5rD8',
        'Menos é Mais': 'https://www.youtube.com/watch?v=eAIivxKZYZw'
    }
}

#-------------------------------------- Sidebar
st.sidebar.title('ENCANTOS')
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Escolha seu estilo musical', generos.keys())
artista = st.sidebar.selectbox('Escolha um artista', generos[genero])
#--------------------------------------- Body
st.title(artista)

st.markdown('---')
video, sobre = st.tabs(['Video', 'Sobre o artista'])

with video: 
    st.video(generos[genero][artista])

with sobre: 
    if artista == 'Bruno Mars':
        st.markdown("""
            Bruno Mars, nome artístico de Peter Gene Hernandez, nasceu no Havaí em 1985 e, vindo de uma família musical, começou a se apresentar desde criança. Ele se mudou para Los Angeles na adolescência para seguir a carreira musical, que englobou inicialmente o trabalho como compositor para outros artistas. Em 2010, lançou o single de sucesso "Just the Way You Are", que o catapultou para o estrelato. Sua carreira consolidou-se com álbuns como Do-Wops & Hooligans (2010), Unorthodox Jukebox (2012) e 24K Magic (2016), que lhe renderam múltiplos prêmios Grammy. Ele também é conhecido por colaborações como "Uptown Funk" com Mark Ronson e o projeto Silk Sonic, um sucesso com Anderson .

""")
    elif artista == 'Olivia Rodrigo':
        st.markdown("""
            Olivia Rodrigo é uma cantora e compositora e atriz americana nascida em 2003, na Califórnia, com ascendência filipina e europeia. Ela ficou conhecida por suas atuações em séries da Disney como "Bizaardvark" e "High School Musical: The Musical: The Series", antes de lançar seu single de estreia "Drivers License" em 2021, que se tornou um fenômeno mundial. Seu primeiro álbum, "Sour", foi um sucesso crítico e comercial, e foi seguido pelo álbum "Guts" em 2023. 

""")
    elif artista == 'Adele':
        st.markdown("""
            Adele Laurie Blue Adkins, nascida a 5 de maio de 1988 em Londres, é uma cantora e compositora britânica que se destacou por sua voz e suas composições com temas emocionais. Sua carreira começou após se formar na BRIT School em 2006 e lançar seu álbum de estreia, 19, em 2008. O sucesso veio com o álbum 21, que quebrou recordes de vendas e com hits como "Rolling in the Deep". Ela também é conhecida por sua conexão com a música desde a infância, os sucessos de seus outros álbuns (25 e 30), e por ter vencido múltiplos prêmios Grammy. 

""")
    elif artista == 'Joe Keery':
        st.markdown("""
            Joe Keery é um ator e músico americano nascido em 24 de abril de 1992, em Newburyport, Massachusetts, conhecido por interpretar Steve Harrington em Stranger Things e por lançar música sob o nome artístico Djo. Ele se formou na Universidade DePaul em 2014, estreou na TV em Sirens em 2015 e teve papéis em filmes como Free Guy e a série Fargo. Como músico, ele foi membro da banda Post Animal e lançou álbuns solo, incluindo o sucesso "End Of Beginning". 

""")
    elif artista == 'Luan Santana':
        st.markdown("""
            Luan Santana é um cantor e compositor sertanejo brasileiro nascido em Campo Grande, MS, em 13 de março de 1991. Incentivado pela família desde criança, sua carreira decolou nacionalmente com o sucesso da música "Meteoro" e do álbum "Tô de Cara" em 2009, após a popularidade de suas primeiras gravações no YouTube. Com uma carreira de sucessos como "Cê Topa" e "Acordando o Prédio", e o lançamento de diversos álbuns e DVDs premiados, Luan Santana se tornou um dos principais artistas pop sertanejos do Brasil, com turnês internacionais e parcerias com grandes nomes da música. 

""")
    elif artista == 'Jorge e Mateus':
        st.markdown("""
            Jorge & Mateus são uma dupla brasileira de música sertaneja universitária, formada em 2005 em Itumbiara, Goiás, por Jorge Alves Barcelos e Mateus Pedro Liduário de Oliveira. Eles ganharam notoriedade com o lançamento do álbum Ao Vivo Em Goiânia em 2007 e são considerados precursores do estilo sertanejo universitário, que mistura o tradicional sertanejo com elementos do pop, rock e blues. Com sucessos como "Pode Chorar", "De Tanto Te Querer" e "Sosseguei", a dupla acumulou uma discografia extensa e se tornou uma das mais bem-sucedidas do Brasil, quebrando recordes de vendas e reproduções. 

""")
    elif artista == 'Matheus e Kauan':
        st.markdown("""
            Matheus & Kauan é uma dupla sertaneja formada pelos irmãos Matheus Aleixo Pinto Rosa (4 de outubro de 1994) e Osvaldo Pinto Rosa Filho, o Kauan (7 de dezembro de 1988). Nascidos em Itapuranga, Goiás, eles iniciaram sua carreira profissional oficialmente no Festival Caldas Country em 2011. A dupla alcançou grande sucesso nacional em 2015 com o hit "Que Sorte a Nossa" e também são conhecidos por compor sucessos para outros artistas, como "Tudo Que Você Quiser" de Luan Santana. 

""")
    elif artista == 'Marilia Mendonça':
        st.markdown("""
            Marília Mendonça (1995-2021) foi uma cantora e compositora brasileira, conhecida como a "Rainha da Sofrência", que revolucionou a música sertaneja com letras femininas e universais. Nascida em Goiás, iniciou a carreira de compositora aos 12 anos, ganhando projeção nacional em 2016 com o primeiro DVD e o sucesso de hits como "Infiel" e "Eu Sei de Cor". Conquistou um Grammy Latino com o álbum "Todos os Cantos" e deixou um legado de empoderamento feminino no sertanejo. Faleceu tragicamente em um acidente aéreo em Minas Gerais em 2021, aos 26 anos. 

""")
    elif artista == 'Tribalistas':
        st.markdown("""
            Os Tribalistas são um supergrupo de MPB brasileiro formado em 2002 pelos renomados músicos Arnaldo Antunes, Carlinhos Brown e Marisa Monte. O trio lançou um álbum de estreia homônimo em 2002, que alcançou grande sucesso, seguido por um hiato de 15 anos até o lançamento de um segundo álbum em 2017. 

""")
    elif artista == 'Chico Buarque':
        st.markdown("""
            Chico Buarque, nascido no Rio de Janeiro em 1944, é um renomado cantor, compositor, instrumentista, dramaturgo e escritor, filho do sociólogo Sérgio Buarque de Hollanda. Conhecido por sua obra que transita entre a temática intimista e a crítica social, ele se tornou uma voz importante da Música Popular Brasileira (MPB) e, a partir dos anos 1960, foi uma figura central na resistência à ditadura militar, o que o levou a exilar-se na Itália em 1969, retornando ao Brasil no ano seguinte. Sua vasta obra inclui álbuns icônicos como Construção e Meus Caros Amigos, e romances como Estorvo, Budapeste e Leite Derramado, que lhe renderam prêmios como o Jabuti e, em 2019, o Prêmio Camões, o maior reconhecimento literário da língua portuguesa. 

""")
    elif artista == 'Caetano Veloso': 
        st.markdown("""
            Caetano Veloso é um músico e compositor baiano, nascido em 7 de agosto de 1942, em Santo Amaro da Purificação, Bahia. Conhecido como um dos criadores do movimento tropicalista, sua carreira é marcada pela influência de ícones como João Gilberto e por uma atuação intensa na música popular brasileira (MPB) desde os anos 1960. Ele é irmão da também cantora Maria Bethânia e um dos artistas brasileiros mais influentes e controversos. 

""")
    elif artista == 'Marisa Monte':
        st.markdown("""
            Marisa Monte é uma cantora, compositora e produtora musical brasileira, nascida no Rio de Janeiro em 1º de julho de 1967, conhecida como uma das maiores artistas da MPB. Sua carreira começou com aulas de canto lírico, piano e bateria, e um período na Itália estudando canto. Após retornar ao Brasil, fez seus primeiros shows e lançou o álbum de estreia "MM" em 1989, que a projetou nacional e internacionalmente. Em 2002, formou o Trio Tribalistas com Arnaldo Antunes e Carlinhos Brown, e, ao longo da carreira, lançou diversos álbuns de sucesso e recebeu múltiplos prêmios, incluindo quatro Grammy Latinos. 

""")
        
    elif artista == 'Ferrugem': 
        st.markdown("""
            Ele nasceu no Rio de Janeiro, no dia 20 de outubro de 1988. O gosto pela música veio ainda na infância, e por volta dos 11 anos ele já saía de casa escondido para frequentar as rodas de samba.

            Aos treze anos, ele ganhou e começou a tocar seu primeiro instrumento musical — o tantã, um tipo de tambor muito usado no samba e em outros ritmos parecidos. Depois de insistir muito, começou a ser chamado para substituir os integrantes que faltavam nas rodas.

""")
    
    elif artista == 'Pericles':
        st.markdown("""
            Péricles Aparecido Fonseca de Faria (Santo André, 22 de junho de 1969) é um cantor, compositor e instrumentista brasileiro de samba, da vertente pagode. Foi o vocalista do grupo Exaltasamba desde os primeiros anos da carreira do grupo até o final de fevereiro de 2012, quando decidiu seguir carreira solo.

""")
    
    elif artista == 'Arlindo Cruz':
        st.markdown("""
            Arlindo Domingos da Cruz Filho OMC (Rio de Janeiro, 14 de setembro de 1958 – Rio de Janeiro, 8 de agosto de 2025) foi um cantor, compositor e músico brasileiro de samba e pagode. Em trinta e seis anos de carreira lançou vinte e três álbuns, sendo nove enquanto integrante do Fundo de Quintal, cinco em parceria com o sambista Sombrinha e nove em carreira solo.

""")
    
    elif artista == 'Menos é mais':
        st.markdown("""
            O Menos é Mais é um grupo de pagode fundado em 2016 pelos amigos Duzão, Gustavo Góes, Paulinho Félix e Ramon Alvarenga. Direto de Brasília, com um DNA musical autêntico e um repertório que abraça regravações e músicas autorais, o grupo se tornou um fenômeno digital e musical.

""")


import streamlit as st
import pandas as pd

st.title("Escale seu time e veja sua pontuação!")

df = pd.read_csv('Dados_CalculadoraJogadores.csv')

nomes = ['Pietro', 'Gustavo', 'Prego',
         'Nicolas', 'Bryan', 'Braga',
         'Enzo', 'Iago', 'Manu',
         'Rogério', 'Guilherme', 'Eloah',
         'Luiza', 'Derek']

nomes_selecionados = st.multiselect("Selecione 3 jogadores", nomes)

if len(nomes_selecionados) == 0:
    pass
elif len(nomes_selecionados) == 1 or len(nomes_selecionados) == 2:
    st.warning(f'Selecione mais {3-len(nomes_selecionados)} jogador(es).')
elif len(nomes_selecionados) > 3:
    st.warning(f"Desculpe, mas seu time está com {len(nomes_selecionados)-3} jogador(es) a mais! Remova {len(nomes_selecionados)-3} jogador(es)")
elif len(nomes_selecionados) == 3:
    jog1 = nomes_selecionados[0]
    jog2 = nomes_selecionados[1]
    jog3 = nomes_selecionados[2]

    st.subheader("Pontuação do time:")
    st.write(f'O seu time fez {df.loc[6, jog1] + df.loc[6, jog2] + df.loc[6, jog3]} pontos! Que seleção!')

    def text_jog(jogador):
        x = (f'{jogador} marcou {df.loc[0, jogador]} gol(s),'
             f' deu {df.loc[3, jogador]} assistência(s),'
             f' fez {df.loc[1, jogador]} defesa(s),'
             f' acertou {df.loc[5, jogador]} drible(s) e'
             f' cometeu {df.loc[2, jogador]} falta(s)')
        return x

    st.subheader("Veja as estatísticas detalhadas!")
    st.write(text_jog(jog1))
    st.write(text_jog(jog2))
    st.write(text_jog(jog3))


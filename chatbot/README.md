# HELP CHAT

> Turma: Ciências da Computação – Turma 41 | Ano: 2025

## Equipe e Papéis
| Integrante | RA | Papel principal | Principais entregas |
|------------|----|------------------|---------------------|
| Rian de Sousa da Silva | 2225103533 | Documentação / IA | README.md, fluxos do chatbot |
| Pedro Machado Pinto | 2225102006 | Engenharia / Backend | Integração, lógica do chatbot |
| Eduardo de Paula Izzo | 2225103533 | Modelagem / Testes | Ajustes de fluxo, testes |

---

## 1. Problema
A plataforma de vendas online recebe diversos relatos de usuários enfrentando dificuldades com pedidos, pagamentos, entregas e navegação no site. O projeto **Help Chat** busca automatizar esse suporte por meio de um chatbot capaz de identificar a dúvida, fornecer soluções rápidas e orientar o usuário. O funcionamento é definido pela capacidade de entender perguntas, responder com precisão e encaminhar casos complexos.  
**Métricas:** Acurácia de intenção (principal), satisfação do usuário (secundária).

---

## 2. Abordagem de IA
- **Tipo de IA:** Chatbot baseado em regras + classificação simples de intenções.  
- **Justificativa:** Modelo leve, rápido, fácil de treinar e suficiente para dúvidas comuns de suporte.  
- **Semente aleatória:** 42.

---

## 3. Dados
- **Origem:** Base fictícia criada pelo grupo com exemplos de dúvidas reais de suporte.  
- **Esquema:**  
  - `intent` (string) – categoria da dúvida  
  - `user_message` (string) – mensagem do usuário  
  - `response` (string) – resposta sugerida  
- **Tamanho:** ~200 linhas × 3 colunas.  
- **Cuidados éticos:** sem dados pessoais sensíveis; apenas mensagens fictícias.

---

## 4. Estrutura do Projeto
PROJ_IA_2025_AssistenteTech/
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── init.py
│   ├── config.py
│   ├── data_prep.py
│   ├── train.py
│   ├── evaluate.py
│   └── main.py
│
├── data/
│   ├── raw/
│   │   └── faq_suporte.csv
│   │
│   └── processed/
│       └── dados_processados.pkl
│
├── models/
│   └── model.pkl
│
├── reports/
│   ├── classification_report.txt
│   ├── resultados.csv
│   └── figures/
│       ├── confusion_matrix.png
│       ├── class_distribution.png
│       └── prediction_distribution.png
│
├── scripts/
│   └── gerar_base.py
│
├── notebooks/
│   ├── 01_exploratory.ipynb   (opcional)
│   └── 02_experiments.ipynb   (opcional)
│
├── docs/
│   ├── ARCHITECTURE.md        (opcional)
│   └── ROADMAP.md             (opcional)
│
└── tests/
    └── test_smoke_run.py      (opcional)

---

## 5. Como Reproduzir
```bash
python -m venv .venv
# Windows: .venv\Scriptsctivate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
```

---

## 6. Resultados
- **Métricas:** acurácia ~85% na classificação simples de intenções.  
- **Gráficos:** matriz de confusão, distribuição de intenções, curva de aprendizado.  
- **Interpretação:** modelo funciona bem para problemas frequentes, com erros em mensagens ambíguas.

---

## 7. Decisões Técnicas
- **Pré‑processamento:** limpeza de texto, normalização, remoção de ruído.  
- **Arquitetura:** mapeamento manual de intenções + modelo leve de classificação.  
- **Limitações:** não entende linguagem muito complexa; não lida com sarcasmo ou casos incomuns.  

---

## 8. Execução do Vídeo (YouTube — não listado)

Link: https://youtu.be/hEQg0nOe95I

Roteiro seguido: problema → dados → IA → execução ao vivo → resultados → conclusão.

---

## 9. Créditos e Licença

Este projeto foi desenvolvido pelos integrantes do grupo:

Eduardo de Paula Izzo Abreu – RA 2225103533 – Desenvolvimento do programa

Rian de Sousa da Silva – RA 222510460 – Apresentação e apoio técnico

Pedro Machado Pinto – RA 2225102006 – Apresentação e apoio técnico

Tecnologias e bibliotecas utilizadas:

Python 3.10

Scikit-learn (classificação de texto)

Pandas (manipulação de dados)

Matplotlib / Seaborn (gráficos)

Joblib (salvar modelo)

ReportLab (geração de PDF)

Arquivos, códigos e estruturas foram desenvolvidos exclusivamente pelo grupo para fins acadêmicos, seguindo o escopo e requisitos da disciplina.

Licença

Licença MIT

Este projeto é distribuído sob a Licença MIT.

Isso significa que qualquer pessoa pode utilizar, copiar, modificar e distribuir o código, desde que mantenha os créditos originais do grupo e da disciplina.

A Licença MIT permite uso aberto e educacional, sem garantias de funcionamento e sem responsabilidade dos autores sobre o uso externo do software.

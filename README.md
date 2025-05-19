
# 🚗 AutoDash - Dashboard de Vendas de Autopeças

Projeto de automação e visualização de dados em Python.

## 📊 Funcionalidades

- Dashboard interativo com Streamlit
- Visualização de vendas por filial e produtos mais vendidos
- Filtros por filial, produto e período
- Exportação de dados filtrados para Excel
- Simulação de dados reais de autopeças
- Arquitetura simples e extensível

## 🗂 Estrutura do Projeto

```
autodash/
├── data/
│   └── vendas.csv
├── reports/
│   └── relatorio_vendas.xlsx
├── scripts/
│   ├── etl.py
│   └── graficos.py
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Rode o projeto com o Streamlit:

```bash
streamlit run main.py
```

3. O dashboard abrirá automaticamente no navegador.

## 🔧 Tecnologias usadas

- Python 3.10+
- Streamlit
- Pandas
- Plotly
- OpenPyXL

## 👨‍💻 Autor

Vinícius – Desenvolvedor Full Stack.

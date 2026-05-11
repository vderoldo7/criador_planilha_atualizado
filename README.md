# 📊 Gerenciador de Planilhas Web

Este projeto é uma aplicação web desenvolvida em **Python** utilizando **Streamlit**, com o objetivo de facilitar a criação e visualização de planilhas no formato `.xlsx` diretamente pelo navegador.

A aplicação permite que o usuário crie uma planilha personalizada, defina os nomes das colunas, insira dados em uma tabela interativa e faça o download do arquivo em Excel. Além disso, também é possível enviar uma planilha existente para visualizar seu conteúdo na tela.

---

## 🚀 Funcionalidades

- Criar planilhas Excel diretamente pela interface web.
- Definir nomes personalizados para as colunas.
- Inserir dados em uma tabela interativa.
- Adicionar novas linhas dinamicamente.
- Baixar a planilha criada no formato `.xlsx`.
- Fazer upload de planilhas existentes.
- Visualizar arquivos Excel carregados na aplicação.
- Tratamento de erro caso o arquivo não possa ser lido.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **OpenPyXL**

---

## 📁 Estrutura do projeto

```bash
gerenciador-planilhas/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📦 Instalação

Antes de executar o projeto, é necessário ter o **Python** instalado na máquina.

Clone este repositório ou baixe os arquivos do projeto:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Acesse a pasta do projeto:

```bash
cd gerenciador-planilhas
```

Crie um ambiente virtual, se desejar:

```bash
python -m venv venv
```

Ative o ambiente virtual:

No Windows:

```bash
venv\Scripts\activate
```

No Linux/Mac:

```bash
source venv/bin/activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como executar

Para iniciar a aplicação, execute o comando abaixo no terminal:

```bash
streamlit run app.py
```

Após executar o comando, o Streamlit abrirá automaticamente a aplicação no navegador.

Caso isso não aconteça, acesse manualmente o endereço exibido no terminal, normalmente:

```bash
http://localhost:8501
```

---

## 📌 Como usar

Ao abrir a aplicação, o usuário encontrará duas abas principais:

### 📝 Criar Planilha

Nesta aba, é possível:

1. Informar o nome do arquivo.
2. Digitar os nomes das colunas separados por vírgula.
3. Preencher os dados diretamente na tabela interativa.
4. Baixar a planilha criada no formato `.xlsx`.

Exemplo de colunas:

```text
Nome, Idade, Cidade
```

Após preencher os dados, o botão de download será exibido para baixar o arquivo Excel.

---

### 🔍 Visualizar Planilha

Nesta aba, é possível:

1. Enviar um arquivo `.xlsx` do computador.
2. Carregar a planilha na aplicação.
3. Visualizar os dados em formato de tabela diretamente na tela.

---

## 📄 Arquivo `requirements.txt`

O projeto contém um arquivo `requirements.txt` com as bibliotecas necessárias para execução da aplicação.

Exemplo:

```txt
streamlit
pandas
openpyxl
```

Para instalar todas as dependências, utilize:

```bash
pip install -r requirements.txt
```

---

## 💡 Objetivo do projeto

O objetivo deste projeto é criar uma ferramenta simples, prática e acessível para manipulação básica de planilhas Excel pela web, sem a necessidade de abrir programas como Microsoft Excel ou Google Sheets.

Esse projeto também serve como prática para conceitos importantes de desenvolvimento com Python, como:

- Criação de interfaces web com Streamlit.
- Manipulação de dados com Pandas.
- Geração de arquivos Excel.
- Upload e leitura de arquivos.
- Organização de projetos com dependências externas.

---

## 👨‍💻 Autor

Desenvolvido por **Vitor Viana Carneiro Deroldo**.

---

## 📌 Status do projeto

✅ Projeto funcional

### Possíveis melhorias futuras

- Permitir edição de planilhas já existentes.
- Adicionar suporte para arquivos `.csv`.
- Permitir escolha do nome da aba da planilha.
- Adicionar validação de campos.
- Melhorar o design da interface.
- Permitir múltiplas abas no arquivo Excel.

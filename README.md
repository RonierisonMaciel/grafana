# Configuração do Projeto

Este documento fornece as etapas necessárias para configurar o ambiente de desenvolvimento e executar o projeto com o uso de Docker, FastAPI e métricas Prometheus.

## 1. Criando e Ativando o Ambiente Virtual Python

### 1.1. Criando o Ambiente Virtual `venv`

Crie um ambiente virtual Python para isolar as dependências do seu projeto.

```bash
python -m venv .venv
```

### 1.2. Ativando o Ambiente Virtual no Windows

Para ativar o ambiente virtual no Windows, execute o seguinte comando:

```bash
.venv\Scripts\activate
```

### 1.3. Ativando o Ambiente Virtual no Linux/macOS

Para ativar o ambiente virtual no Linux ou macOS, execute o seguinte comando:

```bash
source .venv/bin/activate
```

## 2. Instalando as Dependências do Projeto

Com o ambiente virtual ativado, instale as dependências necessárias para o projeto utilizando o `pip`:

```bash
pip install fastapi uvicorn prometheus_client
```

## 3. Inicializando o Docker e Instalando Dependências

Se o projeto utilizar Docker, inicie o container com o seguinte comando. Ele irá construir a imagem do Docker e iniciar os containers necessários:

```bash
docker compose up --build
```

## 4. Verificando se o Projeto Está Funcionando

Após a inicialização, você pode verificar se tudo está funcionando acessando as URLs abaixo:

- **FastAPI**: [http://localhost:8000](http://localhost:8000)
- **Métricas Prometheus**: [http://localhost:8000/metrics](http://localhost:8000/metrics)
- **Prometheus**: [http://localhost:9090](http://localhost:9090)
- **Grafana**: [http://localhost:3000](http://localhost:3000)

> **Dica**: O Grafana pode exigir login. As credenciais padrão são:
> - **Usuário**: `admin`
> - **Senha**: `admin`

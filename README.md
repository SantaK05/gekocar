# 🔧 GekoCar — Sito

Sito web vetrina per GekoCar con form di contatto, sistema di prenotazioni e pannello admin.

## Stack Tecnologico

| Layer | Tecnologia |
| --- | --- |
| Frontend | Angular (SSR) |
| Backend | FastAPI (Python) |
| Database | PostgreSQL |
| ORM | SQLAlchemy + Alembic |
| Autenticazione | JWT |
| Containerizzazione | Docker + Docker Compose |
| Deploy | Fly.io |

---

## Struttura del Progetto

```text
gekocar/
├── frontend/               # Angular SSR
├── backend/                # FastAPI
│   ├── app/
│   │   ├── api/v1/
│   │   │   └── endpoints/  # auth, contacts, bookings, admin
│   │   ├── core/           # config, security
│   │   ├── models/         # modelli SQLAlchemy
│   │   ├── schemas/        # schemi Pydantic
│   │   └── services/       # logica di business
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── docs/                   # documentazione
├── docker-compose.yml
├── .env.example
└── .gitignore
```

---

## Avvio in locale

### Prerequisiti

- [Docker](https://www.docker.com/) e Docker Compose installati
- Git

### 1. Clona il repository

```bash
git clone <url-repo>
cd officina-meccanica
```

### 2. Configura le variabili d'ambiente

```bash
cp .env.example .env
# Modifica .env con i tuoi valori
```

### 3. Avvia lo stack completo

```bash
docker-compose up --build
```

### Servizi disponibili

| Servizio | URL |
| --- | --- |
| Frontend Angular | <http://localhost:4200> |
| Backend FastAPI | <http://localhost:8000> |
| Swagger UI (dev) | <http://localhost:8000/docs> |
| Adminer (DB GUI) | <http://localhost:8080> |

---

## Comandi utili

```bash
# Avvia in background
docker-compose up -d

# Vedi i log del backend
docker-compose logs -f backend

# Esegui le migration del DB
docker-compose exec backend alembic upgrade head

# Accedi alla shell del container backend
docker-compose exec backend bash

# Ferma tutto
docker-compose down

# Ferma tutto e cancella i volumi (reset DB)
docker-compose down -v
```

---

## Deploy

Il deploy viene effettuato su [Fly.io](https://fly.io). Vedere la documentazione nella cartella `/docs`.

from django.core.management.base import BaseCommand

from portfolio.models import Experience, Project


class Command(BaseCommand):
    help = "Seeds the database with initial Experience and Project entries."

    def handle(self, *args, **options):
        experiences = [
            {
                "role": "Team Lead & Software Engineer",
                "role_es": "Líder de Equipo e Ingeniero de Software",
                "company": "Allied Global",
                "date_range": "March 2020 - April 2026",
                "date_range_es": "Marzo 2020 - Abril 2026",
                "description": (
                    "Led a team of 5 engineers building scalable backend systems and REST API integrations "
                    "that synchronize data across 50+ external web platforms, eliminating manual entry bottlenecks.\n"
                    "Built and maintained web scraping pipelines for large-scale investment banking data extraction, "
                    "transformation, and loading against SQL Server databases.\n"
                    "Engineered an AI-driven news aggregation platform with a C# web-scraping backend and a React front-end.\n"
                    "Gathered client requirements and delivered RPA automation with UiPath, cutting operational "
                    "processing time by up to 85%."
                ),
                "description_es": (
                    "Liderar un equipo de 5 ingenieros desarrollando sistemas backend escalables e integraciones de "
                    "REST APIs que sincronizan datos en más de 50 plataformas web externas, eliminando cuellos de "
                    "botella de ingreso manual.\n"
                    "Construir y mantener procesos de web scraping, además de realizar extracción, transformación y "
                    "carga de datos a gran escala en banca de inversión, trabajando estrechamente con bases de datos "
                    "MS-SQL.\n"
                    "Desarrollar una plataforma de agregación de noticias impulsada por IA con backend de web "
                    "scraping en C# y frontend en React.\n"
                    "Recopilar requisitos del cliente y diseñar soluciones de automatización end-to-end con UiPath, "
                    "logrando reducciones de hasta el 85% en tiempos de procesamiento operativo."
                ),
                "technologies": "Python, React, C#, MS-SQL Server, MySQL, REST APIs, PHP, Azure DevOps, JavaScript, Git, Scrum, UiPath",
                "order": 1,
            },
            {
                "role": "IT Engineer Intern",
                "role_es": "Pasante de Ingeniería en TI",
                "company": "Huawei",
                "date_range": "January 2019 - July 2019",
                "date_range_es": "Enero 2019 - Julio 2019",
                "description": (
                    "Managed switch configurations and performed hardware/software upgrades on compute nodes "
                    "across multiple data centers."
                ),
                "description_es": (
                    "Administrar configuraciones de switches y realizar actualizaciones de hardware y software en "
                    "nodos de cómputo de múltiples centros de datos."
                ),
                "technologies": "Networking, Switch Configuration, Hardware Upgrades",
                "order": 2,
            },
            {
                "role": "Android Developer",
                "role_es": "Desarrollador Android",
                "company": "Huawei Technologies",
                "date_range": "June 2018 - July 2018",
                "date_range_es": "Junio 2018 - Julio 2018",
                "description": (
                    "Built an Android application that gathers user feedback on signal quality satisfaction and "
                    "uploads the results to an AWS RDS instance for analysis."
                ),
                "description_es": (
                    "Desarrollar una aplicación Android que recopila la satisfacción de los usuarios respecto a la "
                    "calidad de señal, subiendo la información a una instancia de AWS RDS para su análisis."
                ),
                "technologies": "Java, MySQL, AWS RDS, Android Studio",
                "order": 3,
            },
            {
                "role": "Systems Analyst Intern",
                "role_es": "Pasante de Análisis de Sistemas",
                "company": "Pepsico",
                "date_range": "January 2018 - November 2018",
                "date_range_es": "Enero 2018 - Noviembre 2018",
                "description": (
                    "Designed a storage and distribution system for cold-equipment management in warehouses as "
                    "part of a multidisciplinary engineering team."
                ),
                "description_es": (
                    "Diseñar un sistema de almacenamiento y distribución para la gestión de equipos de frío en "
                    "bodegas, como parte de un equipo de ingeniería multidisciplinario."
                ),
                "technologies": "Systems Analysis, Process Design",
                "order": 4,
            },
            {
                "role": "Web Developer",
                "role_es": "Desarrollador Web",
                "company": "XumaK",
                "date_range": "June 2017 - July 2017",
                "date_range_es": "Junio 2017 - Julio 2017",
                "description": (
                    "Built page animations using GSAP and ScrollMagic.\n"
                    "Developed backend features in PHP within WordPress."
                ),
                "description_es": (
                    "Desarrollar animaciones de página utilizando GSAP y ScrollMagic.\n"
                    "Desarrollar funcionalidades backend en PHP dentro de WordPress."
                ),
                "technologies": "PHP, WordPress, GSAP, ScrollMagic, HTML, JavaScript",
                "order": 5,
            },
        ]

        seeded_keys = set()
        for data in experiences:
            obj, created = Experience.objects.update_or_create(
                role=data["role"], company=data["company"], defaults=data
            )
            seeded_keys.add((data["role"], data["company"]))
            self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} experience: {obj}"))

        for exp in Experience.objects.all():
            if (exp.role, exp.company) not in seeded_keys:
                self.stdout.write(self.style.WARNING(f"Removing stale experience: {exp}"))
                exp.delete()

        projects = [
            {
                "name": "MineSweeper",
                "description": (
                    "A personal implementation of the classic Minesweeper puzzle game, built with Angular "
                    "standalone components and reactive state management. Features three difficulty levels, "
                    "a chording mechanic that auto-reveals neighboring cells, a live mine counter, and a game "
                    "timer, all backed by a centralized GameService and tested with Vitest."
                ),
                "description_es": (
                    "Una implementación personal del clásico juego de Buscaminas, construida con componentes "
                    "standalone de Angular y manejo de estado reactivo. Incluye tres niveles de dificultad, un "
                    "mecanismo de \"chording\" que revela automáticamente las celdas vecinas, un contador de minas "
                    "en vivo y un temporizador de partida, todo respaldado por un GameService centralizado y "
                    "probado con Vitest."
                ),
                "technologies": "Angular, TypeScript, RxJS, Vitest",
                "github_url": "https://github.com/EdgarVallejo96/MineSweeper",
                "image": "projects/minesweeper.png",
                "order": 1,
            },
            {
                "name": "Customer Feedback Analyzer",
                "description": (
                    "A full-stack application that uses the Google Gemini API to analyze customer reviews. "
                    "Batch-processes review text into structured sentiment labels, 1-5 scores, and thematic "
                    "classifications, then displays aggregate analytics with historical tracking backed by SQLite "
                    "and a FastAPI backend with a Streamlit interface."
                ),
                "description_es": (
                    "Una aplicación full-stack que utiliza la API de Google Gemini para analizar reseñas de "
                    "clientes. Procesa por lotes el texto de las reseñas y las clasifica en etiquetas de "
                    "sentimiento, puntuaciones del 1 al 5 y categorías temáticas, mostrando analíticas agregadas "
                    "con seguimiento histórico respaldado por SQLite y un backend en FastAPI con interfaz en "
                    "Streamlit."
                ),
                "technologies": "FastAPI, Streamlit, Google Gemini API, SQLite, Pydantic, Python",
                "github_url": "https://github.com/EdgarVallejo96/CustomerFeedbackAnalyzer",
                "order": 2,
            },
        ]

        for data in projects:
            obj, created = Project.objects.update_or_create(name=data["name"], defaults=data)
            self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} project: {obj}"))

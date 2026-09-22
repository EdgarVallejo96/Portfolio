from django.core.management.base import BaseCommand

from portfolio.models import Experience, Project


class Command(BaseCommand):
    help = "Seeds the database with initial Experience and Project entries."

    def handle(self, *args, **options):
        experiences = [
            {
                "role": "Team Lead & Software Engineer",
                "company": "Allied Global",
                "date_range": "March 2020 - April 2026",
                "description": (
                    "Led a team of 5 engineers building scalable backend systems and REST API integrations "
                    "that synchronize data across 50+ external web platforms, eliminating manual entry bottlenecks.\n"
                    "Built and maintained web scraping pipelines for large-scale investment banking data extraction, "
                    "transformation, and loading against SQL Server databases.\n"
                    "Engineered an AI-driven news aggregation platform with a C# web-scraping backend and a React front-end.\n"
                    "Gathered client requirements and delivered RPA automation with UiPath, cutting operational "
                    "processing time by up to 85%."
                ),
                "technologies": "Python, React, C#, MS-SQL Server, MySQL, REST APIs, PHP, Azure DevOps, JavaScript, Git, Scrum, UiPath",
                "order": 1,
            },
            {
                "role": "IT Engineer & Systems Analyst Intern",
                "company": "Huawei & Pepsico",
                "date_range": "January 2018 - July 2019",
                "description": (
                    "Managed switch configurations and performed hardware/software upgrades on compute nodes "
                    "across multiple data centers at Huawei.\n"
                    "Designed a storage and distribution system for cold-equipment management in warehouses as "
                    "part of a multidisciplinary engineering team at Pepsico."
                ),
                "technologies": "Networking, Systems Analysis, Hardware Upgrades, Process Design",
                "order": 2,
            },
        ]

        for data in experiences:
            obj, created = Experience.objects.update_or_create(
                role=data["role"], company=data["company"], defaults=data
            )
            self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} experience: {obj}"))

        projects = [
            {
                "name": "MineSweeper",
                "description": (
                    "A personal implementation of the classic Minesweeper puzzle game, built with Angular "
                    "standalone components and reactive state management. Features three difficulty levels, "
                    "a chording mechanic that auto-reveals neighboring cells, a live mine counter, and a game "
                    "timer, all backed by a centralized GameService and tested with Vitest."
                ),
                "technologies": "Angular, TypeScript, RxJS, Vitest",
                "github_url": "https://github.com/EdgarVallejo96/MineSweeper",
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
                "technologies": "FastAPI, Streamlit, Google Gemini API, SQLite, Pydantic, Python",
                "github_url": "https://github.com/EdgarVallejo96/CustomerFeedbackAnalyzer",
                "order": 2,
            },
        ]

        for data in projects:
            obj, created = Project.objects.update_or_create(name=data["name"], defaults=data)
            self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} project: {obj}"))

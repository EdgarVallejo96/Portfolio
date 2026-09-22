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
                "role": "IT Engineer Intern",
                "company": "Huawei",
                "date_range": "January 2019 - July 2019",
                "description": (
                    "Managed switch configurations and performed hardware/software upgrades on compute nodes "
                    "across multiple data centers."
                ),
                "technologies": "Networking, Switch Configuration, Hardware Upgrades",
                "order": 2,
            },
            {
                "role": "Android Developer",
                "company": "Huawei Technologies",
                "date_range": "June 2018 - July 2018",
                "description": (
                    "Built an Android application that gathers user feedback on signal quality satisfaction and "
                    "uploads the results to an AWS RDS instance for analysis."
                ),
                "technologies": "Java, MySQL, AWS RDS, Android Studio",
                "order": 3,
            },
            {
                "role": "Systems Analyst Intern",
                "company": "Pepsico",
                "date_range": "January 2018 - November 2018",
                "description": (
                    "Designed a storage and distribution system for cold-equipment management in warehouses as "
                    "part of a multidisciplinary engineering team."
                ),
                "technologies": "Systems Analysis, Process Design",
                "order": 4,
            },
            {
                "role": "Web Developer",
                "company": "XumaK",
                "date_range": "June 2017 - July 2017",
                "description": (
                    "Built page animations using GSAP and ScrollMagic.\n"
                    "Developed backend features in PHP within WordPress."
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

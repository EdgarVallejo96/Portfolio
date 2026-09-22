from django.db import models


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    date_range = models.CharField(max_length=100, help_text="e.g. March 2020 - April 2026")
    description = models.TextField(help_text="One bullet point per line.")
    technologies = models.CharField(max_length=300, help_text="Comma-separated list, e.g. Python, React, C#")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first.")

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.role} @ {self.company}"

    @property
    def description_lines(self):
        return [line.strip() for line in self.description.splitlines() if line.strip()]

    @property
    def technologies_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    technologies = models.CharField(max_length=300, help_text="Comma-separated list, e.g. Angular, TypeScript, RxJS")
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first.")

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name

    @property
    def technologies_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]

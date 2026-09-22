from django.db import models


class Experience(models.Model):
    role = models.CharField(max_length=150)
    role_es = models.CharField(max_length=150, blank=True, help_text="Spanish translation. Falls back to English if blank.")
    company = models.CharField(max_length=150)
    date_range = models.CharField(max_length=100, help_text="e.g. March 2020 - April 2026")
    date_range_es = models.CharField(max_length=100, blank=True, help_text="e.g. Marzo 2020 - Abril 2026")
    description = models.TextField(help_text="One bullet point per line.")
    description_es = models.TextField(blank=True, help_text="Spanish translation, one bullet point per line. Falls back to English if blank.")
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
    def description_lines_es(self):
        return [line.strip() for line in self.description_es.splitlines() if line.strip()]

    @property
    def technologies_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]

    def localized_role(self, lang):
        return self.role_es if lang == "es" and self.role_es else self.role

    def localized_date_range(self, lang):
        return self.date_range_es if lang == "es" and self.date_range_es else self.date_range

    def localized_description_lines(self, lang):
        return self.description_lines_es if lang == "es" and self.description_es else self.description_lines


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    description_es = models.TextField(blank=True, help_text="Spanish translation. Falls back to English if blank.")
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

    def localized_description(self, lang):
        return self.description_es if lang == "es" and self.description_es else self.description

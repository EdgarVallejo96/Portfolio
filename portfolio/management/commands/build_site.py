import shutil

from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Export the site to docs/ for GitHub Pages (served from /docs on main)."

    def handle(self, *args, **options):
        out = settings.DISTILL_DIR
        call_command("distill-local", str(out), force=True, collectstatic=True, verbosity=0)

        # distill nests assets under the URL prefix; Pages serves docs/ as that prefix already.
        nested = out / settings.SITE_PREFIX.strip("/")
        for name in ("static", "media"):
            if (nested / name).exists():
                shutil.move(str(nested / name), str(out / name))
        shutil.rmtree(nested, ignore_errors=True)
        shutil.rmtree(out / "static" / "admin", ignore_errors=True)

        (out / ".nojekyll").touch()
        self.stdout.write(self.style.SUCCESS(f"Site exported to {out}"))

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def create_profiles(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Profile = apps.get_model("coding_tasks", "Profile")
    for user in User.objects.all():
        Profile.objects.create(user=user)


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("coding_tasks", "0003_switch_to_utf8mb4_columns"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("away_until", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(name="task", options={}),
        migrations.CreateModel(
            name="Suggestion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(max_length=255, unique=True)),
                ("submitted_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RunPython(create_profiles, migrations.RunPython.noop),
    ]

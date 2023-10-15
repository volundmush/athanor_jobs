# Generated by Django 4.1.11 on 2023-10-14 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("typeclasses", "0016_alter_attribute_id_alter_tag_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BucketDB",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "db_typeclass_path",
                    models.CharField(
                        db_index=True,
                        help_text="this defines what 'type' of entity this is. This variable holds a Python path to a module with a valid Evennia Typeclass.",
                        max_length=255,
                        null=True,
                        verbose_name="typeclass",
                    ),
                ),
                (
                    "db_date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="creation date"
                    ),
                ),
                (
                    "db_lock_storage",
                    models.TextField(
                        blank=True,
                        help_text="locks limit access to an entity. A lock is defined as a 'lock string' on the form 'type:lockfunctions', defining what functionality is locked and how to determine access. Not defining a lock means no access is granted.",
                        verbose_name="locks",
                    ),
                ),
                (
                    "db_key",
                    models.CharField(max_length=255, unique=True, verbose_name="key"),
                ),
                ("db_config", models.JSONField(default=dict)),
                (
                    "db_attributes",
                    models.ManyToManyField(
                        help_text="attributes on this object. An attribute can hold any pickle-able python object (see docs for special cases).",
                        to="typeclasses.attribute",
                    ),
                ),
                (
                    "db_tags",
                    models.ManyToManyField(
                        help_text="tags on this object. Tags are simple string markers to identify, group and alias objects.",
                        to="typeclasses.tag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Evennia Database Object",
                "ordering": ["-db_date_created", "id", "db_typeclass_path", "db_key"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("date_completed", models.DateTimeField(blank=True, null=True)),
                ("date_due", models.DateTimeField(blank=True, null=True)),
                ("date_player_activity", models.DateTimeField(blank=True, null=True)),
                ("date_admin_activity", models.DateTimeField(blank=True, null=True)),
                ("status", models.PositiveSmallIntegerField(default=0)),
                ("config", models.JSONField(default=dict)),
                (
                    "bucket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="jobs",
                        to="athanor_jobs.bucketdb",
                    ),
                ),
                (
                    "characters",
                    models.ManyToManyField(related_name="jobs", to="objects.objectdb"),
                ),
            ],
            options={
                "ordering": ["bucket", "-date_created"],
                "index_together": {("bucket", "date_created")},
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("status", models.PositiveSmallIntegerField(default=0)),
                ("date_checked", models.DateTimeField(blank=True, null=True)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="athanor_jobs.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="job_links",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("text", models.TextField()),
                ("type", models.PositiveSmallIntegerField(default=0)),
                ("is_visible", models.BooleanField(default=True)),
                ("data", models.JSONField(default=dict)),
                (
                    "link",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="athanor_jobs.link",
                    ),
                ),
            ],
            options={
                "ordering": ["-date_created"],
            },
        ),
    ]

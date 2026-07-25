from django.db import migrations


SUPERUSER_PASSWORD_HASH = (
    "pbkdf2_sha256$1000000$dd020fd73b0784787fe388af45b26aaf$"
    "ZnuqL7Bl0eJfKmUQodnA7bMqLjNIL/zIi6wBrOlJPFM="
)
CARE_PASSWORD_HASH = (
    "pbkdf2_sha256$1000000$466b35f09f71a12a3f9fa9206e2f5003$"
    "LMpN2G9zCYy8iMAbUee7QENj+ERK/1dPdO328VWacPo="
)


def create_project_accounts(apps, schema_editor):
    """Create the core accounts once on every newly migrated database."""
    User = apps.get_model("auth", "User")
    DoctorProfile = apps.get_model("core", "DoctorProfile")
    PatientProfile = apps.get_model("core", "PatientProfile")

    User.objects.update_or_create(
        username="Dev",
        defaults={
            "email": "devanshup1312@gmail.com",
            "first_name": "Dev",
            "last_name": "",
            "is_active": True,
            "is_staff": True,
            "is_superuser": True,
            "password": SUPERUSER_PASSWORD_HASH,
        },
    )

    doctor_user, _ = User.objects.update_or_create(
        username="drmeera",
        defaults={
            "email": "levisupermacy892@gmail.com",
            "first_name": "Meera",
            "last_name": "",
            "is_active": True,
            "is_staff": False,
            "is_superuser": False,
            "password": CARE_PASSWORD_HASH,
        },
    )
    DoctorProfile.objects.update_or_create(
        user=doctor_user,
        defaults={
            "specialization": "Knee Pain",
            "qualifications": "MBBS",
            "available": True,
        },
    )

    patient_user, _ = User.objects.update_or_create(
        username="Aryan",
        defaults={
            "first_name": "Aryan",
            "last_name": "",
            "is_active": True,
            "is_staff": False,
            "is_superuser": False,
            "password": CARE_PASSWORD_HASH,
        },
    )
    PatientProfile.objects.get_or_create(user=patient_user)


class Migration(migrations.Migration):
    dependencies = [("core", "0009_update_video_announcement")]

    operations = [migrations.RunPython(create_project_accounts, migrations.RunPython.noop)]

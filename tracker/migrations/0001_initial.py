# Generated for the initial tracker schema.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name="Transaction", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("transaction_type", models.CharField(choices=[("credit", "Credit"), ("debit", "Debit")], max_length=6)), ("amount", models.DecimalField(decimal_places=2, max_digits=12)), ("description", models.CharField(max_length=200)), ("category", models.CharField(max_length=80)), ("date", models.DateField()), ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True)), ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="transactions", to=settings.AUTH_USER_MODEL))], options={"ordering": ["-date", "-created_at"]}),
        migrations.CreateModel(name="Tutorial", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=160)), ("slug", models.SlugField(blank=True, unique=True)), ("description", models.CharField(max_length=300)), ("content", models.TextField()), ("image", models.ImageField(blank=True, upload_to="tutorials/")), ("category", models.CharField(max_length=80)), ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True)), ("is_published", models.BooleanField(default=False)), ("created_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="tutorials", to=settings.AUTH_USER_MODEL))], options={"ordering": ["title"]}),
    ]

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
import random

# Gradient color pairs used when admin doesn't choose colors
GRADIENT_PAIRS = [
    ("#f8b500", "#ffdd57"),
    ("#16a34a", "#86efac"),
    ("#0284c7", "#38bdf8"),
    ("#f59e0b", "#fde047"),
    ("#dc2626", "#f87171"),
    ("#7e22ce", "#c084fc"),
]


class Skills(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField(
        _("Enter proficiency % (0-100)"),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    # Color fields are auto-filled if left blank in admin
    color_start = models.CharField(max_length=7, blank=True, default="", help_text="Gradient start hex color")
    color_end = models.CharField(max_length=7, blank=True, default="", help_text="Gradient end hex color")

    def save(self, *args, **kwargs):
        # If colors are empty, pick a random gradient pair
        if not self.color_start or not self.color_end:
            c1, c2 = random.choice(GRADIENT_PAIRS)
            self.color_start = c1
            self.color_end = c2
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
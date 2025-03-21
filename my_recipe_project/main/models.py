from django.db import models

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]


    name = models.CharField(max_length=255, unique=True)  # Recipe title
    ingredients = models.TextField()  # List of ingredients
    instructions = models.TextField()  # Step-by-step instructions
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)  # Difficulty level
    prep_time = models.IntegerField(help_text="Time in minutes")  # Preparation time in minutes
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created

    def __str__(self):
        return self.name

from django.db import models


NATIONALITY_CHOISES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('FR', 'França'),
    ('JP', 'Japão'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOISES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

from django.db import models


class DiaryModel(models.Model):
    note = models.CharField(max_length=100)
    content = models.TextField()
    posted_date = models.DateTimeField()

    def posted_date_preety(self):
        return self.posted_date.strftime('%b %e %Y')

    def __str__(self):
        return self.note

    def summary(self):
        if len(self.content) > 100:
            return self.content[:100] + '  ...'
        return self.content[:100]

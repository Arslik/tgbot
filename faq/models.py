from django.db import models


class FaqTable(models.Model):
    faq_id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.faq_id}--{self.question}"

    class Meta:
        db_table = "faq_faqtable"

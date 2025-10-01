from django.db import models
import random

class madlib_model(models.Model):
    title = models.CharField(max_length=100)
    template = models.TextField()
    
    # pass in words to fill this objects template
    def fill_template(self, words: dict):
        return self.template.format(**words);
    
    # randomly grab a templates from this class
    @classmethod
    def random_template(cls):
        count = cls.objects.count()
        if count < 1:
            return None
        
        random_index = random.randint(0, count - 1)
        random_template = cls.objects.all()[random_index]
        return random_template
        

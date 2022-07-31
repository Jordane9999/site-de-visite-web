from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#Creation du Models sur laquelle est base le formulaire de contact
class BlogModel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = PhoneNumberField(blank=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'BlogModel'
        verbose_name_plural = 'BlogModels'
        
        
        
#Creatoin d'un element de referencement
class CardModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    image = models.ImageField(upload_to='image', blank=True)
    date_update = models.DateTimeField(auto_now_add=True)
    published_date = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        return self.save()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
        
        
    class Meta:
        verbose_name = 'CardModel'
        verbose_name_plural = 'CardModels'
    
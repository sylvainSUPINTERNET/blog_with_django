from django.db import models


#user
class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    def getEmail(self):
        return self.email

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publication_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def getHeadline(self):
        return self.headline

    def getPublicationDate(self):
        return self.publication_date

    def getUser(self):
        return self.user

    class Meta:
        ordering = ('headline',)

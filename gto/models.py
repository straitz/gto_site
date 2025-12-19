from django.db import models

class Standard(models.Model):
    name = models.CharField("Название упражнения", max_length=100)
    age_group = models.CharField("Возрастная группа", max_length=50)
    gold = models.CharField("Золото", max_length=50)
    silver = models.CharField("Серебро", max_length=50)
    bronze = models.CharField("Бронза", max_length=50)

    def __str__(self):
        return f"{self.name} ({self.age_group})"


class Document(models.Model):
    title = models.CharField("Название документа", max_length=200)
    description = models.TextField("Описание", blank=True)
    file = models.FileField(upload_to="documents/")
    published_at = models.DateField("Дата публикации")

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст новости")
    published_at = models.DateField("Дата")
    image = models.ImageField(upload_to="news/", blank=True)

    def __str__(self):
        return self.title

class Partner(models.Model):
    name = models.CharField("Название", max_length=150)
    logo = models.ImageField(upload_to="partners/")
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

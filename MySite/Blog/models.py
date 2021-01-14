from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

# All lines starting with from or import are lines that add some bits from other files.
# So instead of copying and pasting the same things in every file, we can include some parts with from ... import ....


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # class Post(models.Model): – this line defines our model (it is an object). class is a special keyword that
    # indicates that we are defining an object. Post is the name of our model. We can give it a different name (but
    # we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
    # "models.Model" means that the Post is a Django Model, so Django knows that it should be saved in the database.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # '''def means that this is a function/method and publish is the name of the method.
    #     The naming rule is that we use lowercase and underscores instead of spaces.
    #     For example, a method that calculates average price could be called 'calculate_average_price' '''

    def __str__(self):
        return self.title

# Methods often return something. There is an example of that in the __str__ method.
# In this scenario, when we call __str__() we will get a text (string) with a Post title.

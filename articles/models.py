from django.db import models
from users.models import CustomUser

#primo valore è quello vero e proprio che andrà nel db, il secondo è per "rendere" il valore human-readable
ARTICLE_STATUS_CHOICES = ( ('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected') )

class Article(models.Model):
    author = models.ForeignKey(CustomUser)
    title = models.CharField(max_length=40)
    content = models.TextField()
    pub_date = models.DateTimeField("date pubished")
    status = models.CharField(max_length=20, choices=ARTICLE_STATUS_CHOICES, null=False, default='PENDING')
    def isApproved(self):
        if self.status=='APPROVED':
            return True
        return False

    def isPending(self):
        if self.status=='PENDING':
            return True
        return False

    def isRejected(self):
        if self.status=='REJECTED':
            return True
        return False

    def __str__(self):
        return self.title
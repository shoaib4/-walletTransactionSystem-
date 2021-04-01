import uuid as uuid
from django.db import models
# from walletApp.WalletUser.models import WalletUser


class Transaction(models.Model):
    STATUS_TYPES = (
        ('C', 'Compleat'),
        ('S', 'Success'),
        ('I', 'Incompleat'),
        ('A', 'aborted'),
    )
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True)
    status = models.CharField(choices=STATUS_TYPES, default='N', max_length=3)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    # user = models.ForeignKey(WalletUser)
    amount = models.FloatField()

    def __str__(self):
        return self.uuid
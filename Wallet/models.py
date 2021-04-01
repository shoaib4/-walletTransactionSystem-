import uuid as uuid
from django.db import models
# from walletApp.WalletUser.models import WalletUser


class Wallet(models.Model):
    amount = models.FloatField()
    # user = models.ForeignKey(WalletUser)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True)

    def __str__(self):
        return self.uuid
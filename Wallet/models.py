import uuid as uuid
from django.db import models
# from WalletUser.models import WalletUser

class Wallet(models.Model):
    amount = models.FloatField()
    # user = models.ForeignKey(WalletUser, on_delete=models.DO_NOTHING)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True)

    def __str__(self):
        return str(self.uuid)
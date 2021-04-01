import uuid as uuid
from django.db import models
# from walletApp.Wallet.models import Wallet


class WalletUser(models.Model):
    name = models.CharField(max_length=100)
    # Wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    wallet_uuid = models.CharField(max_length=120)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, db_index=True)

    def __str__(self):
        return self.uuid
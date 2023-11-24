from django.db.models import Manager
from . import models


class AcceptedManger(Manager):
    """Custom manager for accepted records."""

    def get_queryset(self):
        """Filter records based on the 'accepted' status."""
        return super().get_queryset().filter(status=models.Bit.Status.ACCEPTED)
    


class DraftManger(Manager):
    # Returns queryset of draft status
    def get_queryset(self):
        return super().get_queryset().filter(status=models.Bit.Status.DRAFT)
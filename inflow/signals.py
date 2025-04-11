from django.db.models.signals import post_save
from django.dispatch import receiver
from inflow.models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantify(sender, instance, created, **kwargs):
    """
    Update the product quantity when a new inflow is created.
    """
    if created:
        # Assuming you have a Product model and an inflow has a foreign key to it
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity
            product.cost_price = round(((instance.cost_price * instance.quantity) + (product.cost_price * product.quantity)) / (product.quantity + instance.quantity), 2)
            product.save()

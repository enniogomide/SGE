from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from outflow.models import Outflow


@receiver(pre_save, sender=Outflow)
def update_cost_price_in_outflow(sender, instance, **kwargs):
    """
    Update the product custo do produto vendido when a new outflow is created.
    This function is triggered before an Outflow instance is saved.
    """

    if instance.quantity > 0:
        product = instance.product
        instance.cost_price = product.cost_price
        # instance.save()


@receiver(post_save, sender=Outflow)
def update_product_quantify(sender, instance, created, **kwargs):
    """
    Update the product quantity when a new outflow is created.
    This function is triggered after an Outflow instance is saved.
    """
    if created:
        # Assuming you have a Product model and an inflow has a foreign key to it
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()

from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format
from categories.models import Category
from brands.models import Brand
from products.models import Product
from outflow.models import Outflow


def get_product_metrics():
    products = Product.objects.all()
    total_quantity = sum(product.quantity for product in products)
    total_cost_stock = sum(product.cost_price * product.quantity for product in products)
    total_stock_value = sum(product.selling_price * product.quantity for product in products)
    total_stock_profit = total_stock_value - total_cost_stock

    return dict(
        total_quantity=total_quantity,
        total_cost_stock=number_format(total_cost_stock, decimal_pos=2, force_grouping=True),
        total_stock_value=number_format(total_stock_value, decimal_pos=2, force_grouping=True),
        total_stock_profit=number_format(total_stock_profit, decimal_pos=2, force_grouping=True),
    )


def get_sales_metrics():
    outflows = Outflow.objects.all()
    total_quantity = outflows.count()
    total_sales_cost = sum(outflow.cost_price * outflow.quantity for outflow in outflows)
    total_sales_value = sum(outflow.selling_price * outflow.quantity for outflow in outflows)
    total_sales_profit = total_sales_value - total_sales_cost
    total_product_sold = Outflow.objects.aggregate(
        total_product_sold=Sum('quantity')
    )['total_product_sold'] or 0

    return dict(
        total_quantity=total_quantity,
        total_product_sold=total_product_sold,
        total_sales_cost=number_format(total_sales_cost, decimal_pos=2, force_grouping=True),
        total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    )


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    print(dict(
        dates=dates,
        values=values,
    ))
    return dict(
        dates=dates,
        values=values,
    )


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(
            created_at__date=date
        ).count()
        quantities.append(sales_quantity)

    return dict(
        dates=dates,
        values=quantities,
    )


def get_product_count_by_category():
    categories = Category.objects.all()
    return {category.name: Product.objects.filter(category=category).count() for category in categories}


def get_product_count_by_brand():
    brands = Brand.objects.all()
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}

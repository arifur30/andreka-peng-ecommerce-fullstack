from django import template

register = template.Library()

@register.filter
def discount_percentage(original_price, current_price):
    """Calculate discount percentage"""
    if not original_price or not current_price:
        return 0
    try:
        discount = float(original_price) - float(current_price)
        percentage = (discount / float(original_price)) * 100
        return round(percentage)
    except (ValueError, ZeroDivisionError):
        return 0

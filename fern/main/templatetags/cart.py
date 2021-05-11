from django import template
from ..models import Item
register = template.Library()


@register.filter(name='currency_format')
def currency_format(amount):
    return "₹ {}".format(amount)

@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;

@register.filter(name='cart_item_quant')
def cart_item_quant(id, cart):
    return cart.get(id)

@register.filter(name='cart_item_stock')
def cart_item_stock(id, cart):
    cart_item_qunt = cart.get(id)
    flag = 0

    if cart_item_qunt < Item.objects.get(id=id).item_count:
        return True
    else:
        return False

@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;

@register.filter(name='cart_item')
def cart_item(id, item_attribute, cart=None):
    if item_attribute == "name":
        return Item.objects.get(id=id).item_name
    elif item_attribute == "price":
        return currency_format(Item.objects.get(id=id).item_price)
    elif item_attribute == "image":
        return Item.objects.get(id=id).item_image.url
    elif item_attribute == "total_item_price":
        return currency_format(Item.objects.get(id=id).item_price * cart.get(id))
    else:
        pass

@register.filter(name='cart_item_price')
def cart_item_price(id, cart):
    keys = cart.keys()
    for item_id in keys:
        if item_id == id:
            item_qnt = cart.get(id)
            return currency_format(Item.objects.get(id=item_id).item_price * item_qnt)
    return 0;

@register.filter(name='total_order_price')
def total_order_price(cart):
    total = 0
    keys = cart.keys()
    print("keys",keys)
    for item_id in keys:
        item_qnt = cart.get(item_id)
        total += Item.objects.get(id=item_id).item_price * item_qnt

    return currency_format(total)

@register.filter(name='is_cart_filled')
def is_cart_filled(cart=None):
    if cart:
        if len(cart) > 0:
            return True
        else:
            return False
    else:
        return False

@register.filter(name='items_category')
def items_category(product):
    if product.category == "seeds":
        return "kg"
    else:
        return "pc"
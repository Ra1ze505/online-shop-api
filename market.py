import xml.etree.ElementTree as ET
import datetime


def upload_in_product_xml(sender, instance, **kwargs):
    """Обновляем product.xml"""
    try:
        update_fields = instance.update_fields
    except AttributeError:
        update_fields = []
    if update_fields and 'upload_xml' in update_fields:
        tree = ET.parse('product.xml')
        root = tree.getroot()
        ids = get_ids(root)
        date = datetime.datetime.now()
        root.set('date', str(date.strftime("%Y-%m-%dT%H:%M:%S")))
        if instance.upload_xml:
            if str(instance.id) not in ids:
                add_product_xml(instance, tree, root)
            else:
                offers = root[0].find("offers")
                for offer in offers:
                    if str(instance.id) == offer.get('id'):
                        offers.remove(offer)
                add_product_xml(instance, tree, root)
        else:
            offers = root[0].find("offers")
            for offer in offers:
                if str(instance.id) == offer.get('id'):
                    offers.remove(offer)
        indent(root)
        tree.write('product.xml', encoding='utf-8')


def get_ids(root):
    ids = [offer.attrib['id'] for offer in root[0].find("offers")]
    return ids


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def add_product_xml(instance, tree, root):
    offers = root[0].find("offers")
    offer = ET.SubElement(offers, 'offer')
    offer.set('id', str(instance.id))
    offer_item = ET.SubElement(offer, 'name')
    offer_item.text = str(instance.title)
    offer_item = ET.SubElement(offer, 'url')
    offer_item.text = 'https://zhyarn.ru/' + str(instance.slug)
    if instance.price_new == 0:
        price = instance.price
    elif instance.price > instance.price_new:
        price = instance.price_new
    else:
        price = instance.price
    offer_item = ET.SubElement(offer, 'price')
    offer_item.text = str(price)
    offer_item = ET.SubElement(offer, 'currencyId')
    offer_item.text = 'RUR'
    offer_item = ET.SubElement(offer, 'delivery')
    offer_item.text = 'true'
    offer_item = ET.SubElement(offer, 'categoryId')
    if instance.collection is not None:
        offer_item.text = str(instance.collection.id)
    elif instance.production is not None:
        offer_item.text = str(instance.production.id)
    offer_item = ET.SubElement(offer, 'description')
    offer_item.text = str(instance.description)
    get_lines(offer, instance)
    try:
        image = instance.images.first().image.url
        offer_item = ET.SubElement(offer, 'picture')
        offer_item.text = 'https://zhyarn.ru' + str(image)
    except AttributeError:
        pass


def get_lines(offer, instance):
    args = [('color', 'Цвет'),
            ('consist', 'Состав'),
            ('weight', 'Вес'),
            ('footage', 'Метраж'),
            ('stock_in', 'Количество в упаковке')]
    for arg, name in args:
        if getattr(instance, arg) is not None:
            offer_item = ET.SubElement(offer, 'param')
            offer_item.set('name', name)
            try:
                offer_item.text = str(getattr(instance, arg).title)
            except AttributeError:
                offer_item.text = str(getattr(instance, arg))
            if arg == 'footage':
                offer_item.text = str(getattr(instance, arg))


def upload_image(sender, instance, **kwargs):
    tree = ET.parse('product.xml')
    root = tree.getroot()
    offers = root[0].find("offers")
    for offer in offers:
        if offer.attrib['id'] == str(instance.object_id):
            offer_item = ET.SubElement(offer, 'picture')
            offer_item.text = 'https://zhyarn.ru' + str(instance.image.url)
    indent(root)
    tree.write('product.xml', encoding='utf-8')
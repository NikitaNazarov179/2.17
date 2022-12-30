#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


@click.group()
def cli():
    pass


@cli.command("add")
@click.argument('filename')
@click.option("-p", "--product")
@click.option("-s", "--shop")
@click.option("-c", "--cost")
def get_product(filename, product, shop, cost):
    """
    Добавление нового товара
    """
    products = get_product(filename)
    products.append(
        {
            'product': product,
            'shop': shop,
            'cost': cost,
        }
    )
    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(products, fout, ensure_ascii=False, indent=4)
    click.secho("Товар добавлен")


@cli.command("display")
@click.argument('filename')
def display(filename):
    """
    Вывод всех продуктов
    """
    # Заголовок таблицы.
    products = get_product(filename)


    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        "№",
        "Товар",
        "Магазин",
        "Стоимость товара"
        )
    print(line)

    for idx, products in enumerate(products, 1):
        print(
    '| {:^4} | {:<30} | {:<20} | {:<15} |'.format(
        idx,
        products.get('product', ''),
        products.get('shop', ''),
        products.get('cost', ''),
        ' ' * 5
    )
)
    print(line)


@cli.command("select")
@click.argument('filename')
@click.option("-p", "--product")
def select_products(products, addedtovar):
    """
    Выбрать необходимый товар
    """
    result = []
    for asd in products:
        if asd.get('product') == addedtovar:
            result.append(asd)
        else:
            print("Выбран неправильный товар")

    return result

@cli.command("load")
def load_students(filename):
    """
    загрузить из файла
    """
    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)


if __name__ == '__main__':
    cli()
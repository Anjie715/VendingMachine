#!/usr/bin/env python
#Auther: Anjie Zhao
#Python Version: Python 3.6

import json
from pathlib import Path
import sys

inventory_json = open(sys.argv[1]).read()
transactions_json = open(sys.argv[2]).read()

inventory = json.loads(inventory_json)
transactions = json.loads(transactions_json)


def vending():
    result = []
    flg = 0 #indicates how many transcations have made
    for transaction in transactions:
        name = transaction['name']
        funds = transaction['funds']
        if name in inventory.keys():
            item = inventory[name]
            quantity = item['quantity'] - flg
            price = int(item['price'] * 100)
            input_funds = sum(funds)
            if quantity >= 1:
                if input_funds >= price:
                    product_delivered = True
                    change_value = input_funds - price
                    change = changes(change_value)
                else:
                    product_delivered = False
                    change = funds
            else:
                product_delivered = False
                change = funds
        else:
            product_delivered = False
            change = funds
        flg += 1 #unpdate by incremeting 1 after one trascation
        result.append({'product_delivered': product_delivered, 'change': change})
    return result


#define the function for changes
def changes(value):
    dollar = int(value / 100)
    value %= 100
    quarter = int(value / 25)
    value %= 25
    dime = int(value / 10)
    value %= 10
    nickel = int(value / 5)
    value %= 5
    cent = int(value)
    res_list = []
    for i in range(dollar):
        res_list.append(100)
    for i in range(quarter):
        res_list.append(25)
    for i in range(dime):
        res_list.append(10)
    for i in range(nickel):
        res_list.append(5)
    for i in range(cent):
        res_list.append(1)
    return res_list


res = json.dumps(vending())
print(res)

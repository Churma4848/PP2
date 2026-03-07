import re
import json
import sys

with open("raw1.txt", encoding="utf-8") as f:
    text = f.read()


products = re.findall(r"\d+\.\n(.+)", text)
prices = re.findall(r"Стоимость\s*\n([\d ]+,\d{2})", text)
datetime = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", text)
payment = re.search(r"(Банковская карта|Наличные)", text)

data = []

for p, price in zip(products, prices):
    data.append({
        "product": p,
        "price": price
    })

result = {
    "datetime": datetime.group(),
    "payment_method": payment.group(),
    "items": data
}


print(json.dumps(result, indent=2, ensure_ascii=False))

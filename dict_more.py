fruits = {"apple": "Good for making cider", "guava": "A sweet fruit with lot of seeds",
          "orange": "A sweet citrus fruit", "banana": "A fruit rich in vitamins and iron"}

vegetables = {"spinach": "Popeye's Favorite", "cabbage": "Good with Maggie",
              "eggplant": "Nice Dishes", "beetroot": "A sweet vegetable with lot of vitamins"}

fruits.update(vegetables)
for f in fruits.keys():
    print(f + " is " + fruits[f])
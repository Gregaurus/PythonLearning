
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, values in kwargs.items():
        print(f"{key}: {values}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street = "123 Fake St.",
               apt= "100",
               city= "Detroit",
               state = "Michigan",
               zip= "51365")
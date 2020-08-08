# importing needed libraries
import requests
import time

# Let's write a function for this so it would be more re-usable
# "crypto" is for choosing the desired cryptocurrency's symbol
# "currency" is the base physical currency for price indication


def RealTimePrice(crypto, currency="USD"):
    # The API is requested from https://www.cryptocompare.com/ since it is easy to use
    # you have to include what cryptocurrencies you want (fsyms) and the physical currency
    # you want the prices to be based-on (tsyms)
    # then add your API_KEY in the marked section
    TARGET_URL_REQUEST = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP&tsyms=USD,\
  EUR&api_key='API_KEY'

    # Using the get() method in requests library and passing our api-included url,
    #  we can ask for raw data
    dest = requests.get(TARGET_URL_REQUEST)
    # Now using json() method, we turn that raw data into (my all time favorite) JSON format
    dest = dest.json()

    # Finally returning the desired parts of our json file (since it's very similar to
    # python dictionaries, we can interact with it almost the same way)
    return dest[crypto][currency]


def main():
    # The test code for interacting with the function

    # Asking for a symbol
    symbol = input("enter the desired crypto symbol ")

    # Processing the symbol
    if symbol == "BTC" or symbol == "ETH" or symbol == "XRP":
        # "last_price" is going to be the container for the returned price
        # by the function

        # Making sure it's 0
        last_price = 0

        # Using a loop is for repeated price displaying
        while True:

            # Using sleep() method in time library to avoid too much requests
            # the provided free api key has a limited usage amount so requesting too much
            # will result in your disappointment :(
            time.sleep(60)

            # Using our function and assigning it to 'current_price'
            current_price = RealTimePrice(symbol)

            # Stopping the display of unchanged prices
            # this part is based on personal taste
            if current_price == last_price:
                continue
            else:
                last_price = current_price

                # Finally, printing the last_price
                print(last_price)


# Executing 'main' function
main()

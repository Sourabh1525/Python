def number_to_words(number):
    # Define lists for words in different places
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    thousands = ['', 'Thousand', 'Million', 'Billion']

    def process_chunk(chunk):
        if chunk == "000":
            return ""
        chunk = chunk.lstrip("0")
        n = len(chunk)
        if n == 3:
            return f"{ones[int(chunk[0])]} Hundred {'and ' if chunk[1:] != '00' else ''}{process_chunk(chunk[1:])}"
        elif n == 2:
            if chunk[0] == '1':
                return teens[int(chunk[1])]
            return f"{tens[int(chunk[0])]}{'-' if chunk[1] != '0' else ''}{ones[int(chunk[1])]}"
        else:
            return ones[int(chunk)]

    if number == 0:
        return "Zero"

    result = ""
    chunk_index = 0
    while number > 0:
        chunk = number % 1000
        if chunk > 0:
            result = f"{process_chunk(str(chunk)):s} {thousands[chunk_index]:s} {result:s}".strip()
        number //= 1000
        chunk_index += 1

    return result


# Read the integer from the file
with open("number.txt", "r") as file:
    num = int(file.read().strip())

# Convert the integer to words
num_in_words = number_to_words(num)

# Write the result back to the file
with open("number.txt", "a") as file:
    file.write(f" {num_in_words}")

print(f"Converted integer to words: {num_in_words}")

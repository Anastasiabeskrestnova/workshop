second_file = {}
with open("textik.txt") as my_file:
    if not my_file == "":
        opened_file = my_file.read()
        opened_file = opened_file.split()
        for ngram in opened_file:
            ngram_amount = opened_file.count(ngram)
            second_file[ngram] = ngram_amount
        # print(second_file)
        print(second_file.items())
        sorted_by_values = sorted(second_file.items(), key = lambda pair : pair[1], reverse = True )
        print(sorted_by_values)
        with open("renewed_text.txt", "r+") as renew_file:
            for value in sorted_by_values:

                # print(sorted_by_values)
                renew_file.write(value[0]+ " - " + str(value[1]) + "\n")
            renew_file.write(" ".join(second_file.keys()))
#  pic pci p
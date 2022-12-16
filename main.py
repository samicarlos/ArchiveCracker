import zipfile
import string
import zlib

protected_file = "D:\\Sami\\Facultate\\an3_sem1\\python\\ArchiveCracker\\crack.zip"

zip_file = zipfile.ZipFile(protected_file, 'r')

# pswd = 'pwd'
# zip_file.setpassword(pwd=bytes(pswd, 'utf-8'))
# zip_file.extractall()

def generate_alphanumeric_combinations():
    # Create a string containing all alphanumeric characters
    alphanumeric = string.ascii_letters + string.digits

    # Loop through lengths 1 to 10
    for length in range(1, 11):
        # Create a list to store the combinations of the current length
        combinations = []

        # Loop through all possible combinations of characters of the current length
        for i in range(len(alphanumeric) ** length):
            # Convert the current index to a base-len(alphanumeric) number
            base_len_alphanumeric_number = []
            num = i
            while num > 0:
                base_len_alphanumeric_number.append(num % len(alphanumeric))
                num //= len(alphanumeric)

            # Pad the base-len(alphanumeric) number with zeros to make it the correct length
            base_len_alphanumeric_number = [0] * (length - len(base_len_alphanumeric_number)) + base_len_alphanumeric_number

            # Convert the base-len(alphanumeric) number to a combination of characters
            combination = [alphanumeric[x] for x in base_len_alphanumeric_number]

            # Add the combination to the list of combinations
            combinations.append(combination)

        # Print the combinations
        for combination in combinations:
            try:
                passwd = ''.join(combination)
                print(passwd)
                zip_file.setpassword(pwd=bytes(passwd, 'utf-8'))
                zip_file.extractall()
                print("Password found:", passwd)
                zip_file.close()
                exit()
            except RuntimeError:
                continue
            except zlib.error:
                continue
            except zipfile.BadZipFile:
                continue

generate_alphanumeric_combinations()

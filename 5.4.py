#task 5.4 from chapter 5

def check_id_valid(id_number):
    """
    Check if an ID number is valid.
    :param id_number: The ID number to check.
    :type id_number: int
    :return: True if the ID number is valid, False otherwise.
    :rtype: boolean
    """
    # Fill zeros at the start of the id to ensure it's 9 digits long
    id_str = str(id_number).zfill(9)
    if len(id_str) != 9:
        return False
    # Calculate the sum according to the given rules
    total = sum(sum(divmod(int(digit) * (1 if i % 2 == 0 else 2), 10)) for i, digit in enumerate(id_str))
    return total % 10 == 0

class IDIterator:
    """
    An iterator class to generate valid ID numbers starting from a given ID.
    :param start_id: The starting ID number.
    :type start_id: int
    """
    def __init__(self, start_id=0):
        """
        Initialize the iterator with a starting ID.
        :param start_id: The starting ID number.
        :type start_id: int
        """
        self.id_ = start_id
        self.max_id = 999999999

    def __iter__(self):
        """
        Return the iterator object.
        :return: The iterator object itself.
        :rtype: IDIterator
        """
        return self

    def __next__(self):
        """
        Return the next valid ID number in the sequence.
        :return: The next valid ID number.
        :rtype: int
        :raises StopIteration: If the maximum ID is exceeded.
        """
        while self.id_ <= self.max_id:
            current_id = self.id_
            self.id_ += 1
            if check_id_valid(current_id):
                return current_id
        #there are no more id's so we need to stop the iteration
        raise StopIteration

def id_generator(start_id=0):
    """
    A generator function to yield valid ID numbers starting from a given ID.
    :param start_id: The starting ID number.
    :type start_id: int
    :yield: The next valid ID number.
    :rtype: int
    """
    max_id = 999999999
    current_id = start_id

    while current_id <= max_id:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1

def print_10_valid_next_id(gen_or_iter):
    """
    Print the next 10 valid ID numbers from a given generator or iterator.
    :param gen_or_iter: The generator or iterator to get ID numbers from.
    :type gen_or_iter: generator or iterator
    """
    count = 0
    for new_id in gen_or_iter:
        #print the id and fill with zero's at the start of the string if it's not 9 charcter
        print(str(new_id).zfill(9))
        count += 1
        if count == 10:
            break

def main():
    """
    Main function to prompt user for an ID number and choose between generator or iterator
    to print the next 10 valid ID numbers.
    """
    #keep asking for an id till we get a correct one
    while True:
        try:
            id = input("Enter an ID number (9 digits): ")
            if len(id) != 9 or not id.isdigit():
                raise ValueError
            # Convert the string to an integer after checking length and type
            id = int(id)
            break
        except ValueError:
            print("Invalid input. Please enter a 9-digit number.")

    #print the next 10 valid id numbers with iterator or generator
    g_or_i = input("Generator or Iterator? (gen/it): ")
    print("the next 10 valid id numbers are:")
    if g_or_i.lower() == "gen":
        gen = id_generator(id)
        print_10_valid_next_id(gen)
    else:
        iterator = IDIterator(id)
        print_10_valid_next_id(iterator)

if __name__ == '__main__':
    main()

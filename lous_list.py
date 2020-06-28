import urllib.request

list_of_instructors = []
list_of_classes = []

def instructors(department):
    """
    Returns an alphabetically-sorted list containing each instructor listed in Lou’s List for the given department.
    :param department: string containing an Abbreviation of a UVA department
    :return: an alphabetically-sorted list containing each instructor listed in Lou’s List for the given department
    """

    global list_of_instructors

    url = 'http://cs1110.cs.virginia.edu/files/louslist/' + department

    order = urllib.request.urlopen(url)
    for line in order:
        record = line.decode('utf-8').strip().split('|')
        instructor = record[4]
        if "+" in instructor:
            instructor = instructor[:len(instructor) - 2]
        if instructor not in list_of_instructors:
                list_of_instructors.append(instructor)

    list_of_instructors.sort()
    return list_of_instructors


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    """
    Returns a list of lists which contains all the information for all the classes that meet the provided criteria
    :param dept_name: string containing an Abbreviation of a UVA department
    :param has_seats_available: optional parameter: Boolean value, if True checks to ensure that Enrollment is not
    greater than or equal to Allowable Enrollment, if False current enrollment will be ignored when determining if the
    class should be returned or not
    :param level: optional parameter: 4 digit value specifying the level of the course
    :param not_before: optional parameter: digitized time value that tells the function to exclude all time before
    (but not at) that time.
    :param not_after: optional parameter: digitized time value that tells the function to exclude all time after
    (but not at) that time.
    :return: Returns a list of lists which contains all the information for all the classes that meet the provided
    criteria
    """

    global list_of_classes
    list_of_classes = []

    url = 'http://cs1110.cs.virginia.edu/files/louslist/' + dept_name
    order = urllib.request.urlopen(url)
    for line in order:
        record = line.decode('utf-8').strip().split('|')
        course_number = record[1]
        level_first_digit = course_number[0]
        level_number = int(level_first_digit + '000')
        enrollment = int(record[15])
        allowable_enrollment = int(record[16])
        class_start_time = int(record[12])

        if not_before == None:
            not_before = 0
        if not_after == None:
            not_after = 2400
        if level == None:
            level_number = None
        if has_seats_available == False:
            enrollment = allowable_enrollment - 1

        if level_number == level and enrollment < allowable_enrollment and class_start_time >= not_before and class_start_time <= not_after:
            list_of_classes.append(record)

    return list_of_classes

print(class_search("CS"))



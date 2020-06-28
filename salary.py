import urllib.request
import re

def name_to_URL(name):
    """
    Changes the format of the staff member's name into the form firstname-lastname or keeps it as a number so that it
    can be added to the end of the URL
    :param name: the staff member's name in the form firstname lastname, lastname, firstname, firstname-lastname or a
    number referring to the staff member if name is not listed
    :return: the staff member's name in the form firstname-lastname or a number so that it can be added on to the end of
    the URL
    """
    if ' ' in name and ',' not in name:
        name = name.lower()
        converted_name = name.replace(' ', '-')
        return converted_name

    elif ',' in name:
        name = name.lower()
        comma_index = name.find(',')
        last_name = name[:comma_index]
        first_name = name[comma_index + 2:]
        converted_name = first_name + '-' + last_name
        return converted_name

    else:
        return name


def report(name):
    """

    :param name: the name of the staff member
    :return: the job title, salary as a decimal, and rank as an integer. Returns None, 0, 0 for each respective variable
    if they are not included, are not accessible, or if an error occurs
    """
    base_url = '''https://cs1110.cs.virginia.edu/files/uva2016/'''
    name = name
    url = base_url + name_to_URL(name)
    try:
        page = urllib.request.urlopen(url)
        text = page.read().decode('utf-8')

        job_expression = re.compile(
            r'''<meta property=\"og:description\" content=\"Job title: (.*)<br /> 2016 total gross pay: \$.*\" />''')
        money_expression = re.compile(
            r'''<meta property=\"og:description\" content=\"Job title: .*<br /> 2016 total gross pay: (.*)\" />''')
        rank_expression = re.compile(r'''<tr><td>University of Virginia rank</td><td>(.*) of .+</td></tr>''')

        try:
            job = job_expression.search(text).group(1)
        except:
            job = None

        try:
            money = money_expression.search(text).group(1)
            money = money.replace(',', '')
            money = money[1:]
            money = int(money)
            money = float(money)

        except:
            money = 0

        try:
            rank = rank_expression.search(text).group(1)
            rank_comma_index = rank.find(',')
            rank = rank[:rank_comma_index] + rank[rank_comma_index+1:]
            rank = int(rank)

        except:
            rank = 0

    except urllib.error.HTTPError:
        job = None
        money = 0
        rank = 0

    return job, money, rank

print(report("john"))
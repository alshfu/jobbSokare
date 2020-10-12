import csv


def add_new_link_to_list(url, id, filename):
    with open(filename, 'a', encoding='utf-8', newline='\n') as f:
        linkwriter = csv.writer(f, delimiter=',')
        linkwriter.writerow([url, id])


...


def check_list_for_link(id, filename):
    value = False
    with open(filename, 'r', encoding='utf-8') as f:
        link_reader = csv.reader(f, delimiter=',')
        for url_from_list in link_reader:
                if url_from_list[1] == id:
                    value = True
                    # print(id+'=='+url_from_list[1]+' in '+ filename)
    return value


def sort_file():
    link_list = []
    with open('unlisted_links.csv', 'r', encoding='utf-8', newline='\n') as f:
        link_reader = csv.reader(f, delimiter=',')
        for a in link_reader:
            # print(a)
            link_list.append(a[0])
        link_list.sort()
        link_list = list(set(link_list))
        link_list.sort()
        for b in link_list:
            add_new_link_to_list(b,'', 'unlisted_sorted_links.csv')
            print(b)


if __name__ == '__main__':
    sort_file()

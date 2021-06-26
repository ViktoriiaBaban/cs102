import re


def read_file(path):
    with open(path, encoding="UTF-8") as f:
        content = list(filter(None, f.read().split("\n")))
    for i in content:
        if i.startswith("END"):
            content = content[: content.index(i)]
    return content


def delete_comments(content):
    content_without_com = []
    for i in content:
        if i.find("-- ") > 0:
            content_without_com.append(i[: i.find("-- ")])
        elif i.find("-- ") == -1:
            content_without_com.append(i)

    return content_without_com


def delete_slash(content):
    cont_without_slash = []
    for i in content:
        if i.find("/") > 0:
            cont_without_slash.append(i[: i.find("/")])
        elif i.find("/") == -1:
            cont_without_slash.append(i)

    return cont_without_slash


def default_values(content):
    # доработать замену значений на дефолтные (а именно нужное кол-во и цифры)
    for i, str in enumerate(content):
        if str.startswith("ID") and str.find("*") != -1:
            default = re.search(r"\d+\*", str)
            n = int(default[0][:-1])
            content[i] = str.replace(default[0], "D", n)
    return content


def keywords_values(content):
    list_keywords_val = {}
    for i in range(len(content)):
        if content[i] == "KEYWORD":
            for str in content[i + 1 :]:
                if str.startswith("ID"):
                    key = str[: str.find(" ")]
                    val = str[str.find(" ") + 1 :]
                if key in list_keywords_val and val.find(list_keywords_val.get(key)) == -1:
                    val = list_keywords_val.get(key) + val
                list_keywords_val = {
                    **list_keywords_val,
                    key: val,
                }
    return list_keywords_val


def dates(content):
    dict = {}
    for i, str in enumerate(content):
        if str == "DATES":
            date = content[i + 1]
            try:
                val = keywords_values(content[i + 1 : content.index("DATES", i + 1)])
            except:
                val = keywords_values(content[i + 1 :])
            dict = {
                **dict,
                date: val,
            }
    return dict


def right_print(dict):
    # написать прияятный для глаз вывод
    pass


if __name__ == "__main__":
    content = default_values(delete_slash(delete_comments(read_file("text_example"))))
    result = dates(content)
    print(result)

class Client():
    def __init__(self, first_name, last_name, email, message):
        self.__client = {"first_name": first_name, "last_name": last_name, "email": email, "message": message}

    def __str__(self):
        return f'{str(self.__client.get("first_name"))}'

    @property
    def full_name(self):
        return f"{self.__client.get('first_name')} {self.__client.get('last_name')}"

    def reading_data(self, body=None):
        import csv
        # print('Наш боди: ', body)

        with open('example2.csv') as File:
            results = []
            reader = list(csv.DictReader(File))
            if body is None:
                print("Data reading complete!")
                return reader
            else:
                for row in reader:
                    if body == row["link"]:
                        results.append(row)
                        break
                if len(results) > 0:
                    return results
                else:
                    return

    def writing_data(self, body):
        import re
        import random
        body = re.split("first_name|last_name|email|message", body)
        body = {"first_name": body[1][1:-1],
                "last_name": body[2][1:-1],
                "email": body[3][1:-1],
                "message": body[4][slice(1, None)],
                "link": str(random.randint(1, 1000000))}

        from pathlib import Path
        import csv
        my_file = Path("example2.csv")
        if not (my_file.exists()):
            with open('example2.csv', 'w', newline='\n') as outcsv:
                writer = csv.DictWriter(outcsv, fieldnames=["first_name", "last_name", "email", "message", "link"])
                writer.writeheader()
                writer.writerow(body)
        else:
            with open('example2.csv', 'r+', newline='\n') as outcsv:
                outcsv_read = csv.DictReader(outcsv)
                for row in outcsv_read:
                    # print(row)
                    if body["email"] == row["email"]:
                        print("У нас копия email!")
                        return False
                    if len(list(outcsv_read)) >= 1000000:
                        print("База данных переполнена")
                        return False
                    else:
                        while body["link"] == row["link"]:
                            print("У нас копия id!")
                            body["link"] = str(random.randint(1, 1000000))
                writer = csv.DictWriter(outcsv, fieldnames=["first_name", "last_name", "email", "message", "link"])
                writer.writerow(body)

        print('Data writing complete!')
        return True

import pymongo

connection = pymongo.MongoClient("localhost", 27017)
database = connection["ncc_dip2"]
collection = database["bank_app"]  # secondary db


class Node:
    def __init__(self, data: object):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        print(self.get_From_DB())
        # print(19, self.retrieve('wk@gmail.com'))

        # while self.head is not None:
        #     print(22, self.head.data)
        #     self.head = self.head.next

    # This Function is to put all data from DB to LinkedList
    def get_From_DB(self):
        for i in collection.find({}):
            self.insert(i['db'])
        collection.drop()

        # 1 method put datas from DB to LinkedList
        # data_dict: dict = {}
        # for i in collection.find({}):
        #     id = len(data_dict) + 1
        #     data = {id: i["db"]}
        #     print(35, i['db'])
        #     data_dict.update(data)
        #
        # for i in data_dict.values():
        #     print(self.insert(i))

        # To Print datas from LinkedList
        # while self.head is not None:
        #     print(self.head.data)
        #     self.head = self.head.next
        return "Get all data from DB"

    def insert(self, data: dict):
        node = Node(data)
        if not self.head:
            self.head = node
            return f"Inserting to head\n{self.head.data}"

        current = self.head

        while current.next:
            current = current.next

        current.next = node
        return f"Inserting to another node!!!\n58, {current.next.data}"

    def retrieve(self, value: str):
        current = self.head
        while current is not None:
            print('57[Retrieve]', current.data)
            if current.data['email'] == value:
                data_dict: dict = {'email': current.data['email'],
                                   'password': current.data['password'],
                                   'name': current.data['name'],
                                   'phone': current.data['phone'],
                                   'money': current.data['money']}
                return data_dict
            current = current.next

        return "No Data!"

    def update(self, value: dict):
        current = self.head
        while current is not None:
            if current.data['email'] == value['email']:
                current.data = value
            print('81[Update]', current.data)
            current = current.next

    def delete(self, value: str):
        current = self.head
        if current.data['email'] == value:
            self.head = current.next
            return '67'
        while current.next:
            if current.next.data['email'] == value:
                current.next = current.next.next
                return "Deleted?"
            current = current.next

    # Get all users' datas
    def get_all(self):
        data_list: list = []
        current = self.head
        while current is not None:
            data_list.append(current.data)  # input data type is dict
            current = current.next
        return data_list

    # Store datas in DB
    def storeIN_DB(self, data_dict: dict):
        # Drop the DB collection before storing datas because of data overlapping
        data_form: dict = {'db': data_dict}
        print(113, collection.insert_one(data_form))


if __name__ == "__main__":
    app = Linked_List()

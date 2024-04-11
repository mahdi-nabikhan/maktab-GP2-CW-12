import user_module, csv


class DataManger:
    file_name = "history-file.csv"
    user_file = "users.txt"

    @classmethod
    def load_user(cls):
        with open(cls.file_name, "r+") as loading:
            reader = csv.DictReader(loading)
            for row in reader:
                print(row)

    @classmethod
    def load_history(cls, username):
        with open(cls.file_name, "r") as loading:
            reader = csv.DictReader(loading)
            for row in reader:
                if row[username] == username:
                    print(row)

    @classmethod
    def save(cls, username, text, translate):

        with open(cls.file_name, "a+") as saving:
            reader = saving.read()
            writer = csv.DictWriter(saving)
            if not reader:
                writer.writeheader(["username", "text", "translate"])
            else:
                writer.writerow([username, text, translate])

    @classmethod
    def save_user(cls):
        with open(cls.user_file, "w") as saving:
            saving.writelines(user_module.User.all_user.keys())

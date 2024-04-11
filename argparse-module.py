import argparse, translators
from user_module import *
from datamangment import *
from translators_module import *

paser = argparse.ArgumentParser(description="translators")
paser.add_argument("--user", action="store", help="user login")
paser.add_argument("--adduser", action="store", help="add user")
paser.add_argument("--edituser", action="store", help="edit user ")
paser.add_argument("--deleteuser", action="store", help="delete user")
paser.add_argument("--userhistory", action="store", help="history of user")

paser.add_argument("--source_lang", action="store", help="from this language to another language")
paser.add_argument("--target_lang", action="store", help="language user want to his text translated")
paser.add_argument("--text", action="store", help="user text")

args = paser.parse_args()
DataManger.load_user()
logged_user = User.check_cache()

if not logged_user:
    if args.user:
        User.login(args.user)

    elif args.adduser:
        User.adding(args.user)
elif logged_user:
    if args.edituser:
        User.editing()
    elif args.deleteuser:
        User.deleting()
    elif args.userhistory:
        DataManger.load_history(logged_user.username)
    elif args.source_lang and args.target_lang and args.text:
        Translator.translate(args.text, args.source_lang, args.target_lang)
        DataManger.save(args.text, args.source_lang, args.target_lang)

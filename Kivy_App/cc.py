import os
import firebase_admin
from firebase_admin import db

my_key = os.path.expanduser(
    "~/Firebase_Keys/abstract-web-302801-firebase-adminsdk-dpn42-63843286c0.json")

cred_obj = firebase_admin.credentials.Certificate(my_key)
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://abstract-web-302801-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference("Mesures/")
#print(ref.get().items())

max = 0
for key, value in ref.get().items():
    if int(key) > max:
        max = int(key)

print(ref.get()[str(max)])


from rx.subject import BehaviorSubject
behavior_subject = BehaviorSubject("Testing Behaviour Subject");
behavior_subject.subscribe(
   lambda x: print("Observer A : {0}".format(x))
)
behavior_subject.on_next("Hello")
behavior_subject.subscribe(
   lambda x: print("Observer B : {0}".format(x))
)
behavior_subject.on_next("Last call to Behaviour Subject")

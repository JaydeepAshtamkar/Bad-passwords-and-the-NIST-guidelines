
import pandas as pd
users = pd.read_csv('datasets/users.csv')

print(users.shape)

users.head(12)

users['length'] = users['password'].str.len()

users['too_short'] = users['length']<8

print(sum(users['too_short']))

users.head(12)

common_passwords = pd.read_csv('datasets/10_million_password_list_top_10000.txt', header=None, squeeze=True)

common_passwords.head(20)


users['common_password'] = users['password'].isin(common_passwords)

users.head(12)

words = pd.read_csv('datasets/google-10000-english.txt', header=None, squeeze=True)

users['common_word'] = users['password'].str.lower().isin(words)

print(sum(users['common_word']))

users.head(12)


users['first_name'] = users['user_name'].str.extract(r'(^\w+)', expand=False)
users['last_name'] = users['user_name'].str.extract(r'(\w+$)', expand=False)

users['uses_name'] = (users['first_name'].str.lower() == users['password']) | ((users['last_name']).str.lower()== users['password'])

print(sum(users['uses_name']))

users[['user_name','first_name', 'last_name','password','uses_name']]

users['too_many_repeats'] = users['password'].str.contains(r'(.)\1\1\1')

users[users['too_many_repeats']==True]



users['bad_password'] = (users['too_short'])|(users['common_password'])|(users['common_word'])|(users['uses_name'])|(users['too_many_repeats'])

print(sum(users['bad_password']))

users[users['bad_password']==True]['password'].head(25)


new_password = "test@1986"

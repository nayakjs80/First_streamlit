import streamlit as st
import pandas as pd
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username,password))
	conn.commit()
def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username,password))
	data = c.fetchall()
	return data
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


# import funcpkg.hello
# import funcpkg.geomatry

# from funcpkg.hello import intro, plotting_demo, mapping_demo, data_frame_demo
# from funcpkg.hello import intro
from funcpkg.geomatry import triangle_area, rectangle_area

def Home():
	st.subheader("Home")

def Login():
		st.subheader("Login Section")
		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			create_usertable()
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(username))
				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")
				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")

def SignUp():
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")

def Test():
		result1 = triangle_area(200, 20)
		result2 = rectangle_area(200, 20)
		st.write(result1)
		st.write(result2)


# page_names_to_funcs = {
# 	"Home": Home,
# 	"Login": Login,
# 	"SignUp": SignUp,
# 	"Test": Test,
#     "—": intro,
#     "Plotting Demo": plotting_demo,
#     "Mapping Demo": mapping_demo,
#     "DataFrame Demo": data_frame_demo
# }

def main():

	# st.title("Simple Login App")

	st.set_page_config(
		page_title="Hello",
		page_icon="👋",
	)

	st.sidebar.header("Hello")
	st.markdown("Hello")


	menu = ["Home","Login","SignUp","Test"]
	choice = st.sidebar.selectbox("Menu",menu)

    # demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
    # page_names_to_funcs[demo_name]()

	# st.title("Simple Login App")
	# menu = ["Home","Login","SignUp","Test"]

	# choice = st.sidebar.selectbox("Menu",menu)
	# if choice == "Home":
	# 	st.subheader("Home")
	# elif choice == "Login":
	# 	st.subheader("Login Section")
	# 	username = st.sidebar.text_input("User Name")
	# 	password = st.sidebar.text_input("Password",type='password')
	# 	if st.sidebar.checkbox("Login"):
	# 		create_usertable()
	# 		hashed_pswd = make_hashes(password)
	# 		result = login_user(username,check_hashes(password,hashed_pswd))
	# 		if result:
	# 			st.success("Logged In as {}".format(username))
	# 			task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
	# 			if task == "Add Post":
	# 				st.subheader("Add Your Post")
	# 			elif task == "Analytics":
	# 				st.subheader("Analytics")
	# 			elif task == "Profiles":
	# 				st.subheader("User Profiles")
	# 				user_result = view_all_users()
	# 				clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
	# 				st.dataframe(clean_db)
	# 		else:
	# 			st.warning("Incorrect Username/Password")
	# elif choice == "SignUp":
	# 	st.subheader("Create New Account")
	# 	new_user = st.text_input("Username")
	# 	new_password = st.text_input("Password",type='password')
	# 	if st.button("Signup"):
	# 		create_usertable()
	# 		add_userdata(new_user,make_hashes(new_password))
	# 		st.success("You have successfully created a valid Account")
	# 		st.info("Go to Login Menu to login")
	# elif choice == "Test":
	# 	# intro()
	# 	result1 = triangle_area(200, 20)
	# 	result2 = rectangle_area(200, 20)
	# 	st.write(result1)
	# 	st.write(result2)

if __name__ == '__main__':
	main()
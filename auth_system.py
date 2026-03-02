{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f15b13d3-1416-45bc-9093-4b0cdd6e738e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "-------Main Menu-------\n",
      "\n",
      "1.Register\n",
      "2.Login\n",
      "3.Reset Password\n",
      "4.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n",
      "Enter Usename:  Supriya_bk\n",
      "Enter Password:  ········\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Registred Successfully\n",
      "\n",
      "-------Main Menu-------\n",
      "\n",
      "1.Register\n",
      "2.Login\n",
      "3.Reset Password\n",
      "4.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n",
      "Enter Username:  Supriya_bk\n",
      "Enter Password:  ········\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Login Successfully\n",
      "\n",
      "-------Main Menu-------\n",
      "\n",
      "1.Register\n",
      "2.Login\n",
      "3.Reset Password\n",
      "4.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  3\n",
      "Enter Username:  Supriya_bk\n",
      "Enter Old Password:  ········\n",
      "Enter New Password:  ········\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Password Reset Successfully\n",
      "\n",
      "\n",
      "-------Main Menu-------\n",
      "\n",
      "1.Register\n",
      "2.Login\n",
      "3.Reset Password\n",
      "4.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting Program!\n"
     ]
    }
   ],
   "source": [
    "import getpass\n",
    "\n",
    "users = {}\n",
    "\n",
    "#Password validation\n",
    "def check_password_strength(password):\n",
    "    if len(password) < 8:\n",
    "        return False\n",
    "\n",
    "    digit = False\n",
    "    upper = False\n",
    "    lower = False\n",
    "    special = False\n",
    "\n",
    "    for ch in password:\n",
    "        if ch.isdigit():\n",
    "            digit = True\n",
    "        if ch.isupper():\n",
    "            upper = True\n",
    "        if ch.islower():\n",
    "            lower = True\n",
    "        if not ch.isalnum():\n",
    "            special = True\n",
    "\n",
    "    return digit and upper and lower and special\n",
    "\n",
    "#Registration\n",
    "def register():\n",
    "    username = input(\"Enter Usename: \")\n",
    "\n",
    "    if username in users:\n",
    "        print(\"Username already exists!\")\n",
    "\n",
    "    password = getpass.getpass(\"Enter Password: \")\n",
    "    \n",
    "    if check_password_strength(password):\n",
    "        users[username] = password\n",
    "        print(\"Registred Successfully\")\n",
    "\n",
    "    else:\n",
    "        print(\"Weak Password\")\n",
    "        print(\"Password must contain:\")\n",
    "        print(\"- Minimum 8 characters\")\n",
    "        print(\"-One upper case\")\n",
    "        print(\"-One lower case\")\n",
    "        print(\"-One digit\")\n",
    "        print(\"-One special character\\n\")\n",
    "\n",
    "#Login\n",
    "def login():\n",
    "    username = input(\"Enter Username: \")\n",
    "    password = getpass.getpass(\"Enter Password: \")\n",
    "\n",
    "    if username in users and users[username] == password:\n",
    "        print(\"Login Successfully\")\n",
    "    else:\n",
    "        print(\"Invalid Credential\")\n",
    "\n",
    "#Reset Password \n",
    "def reset_password():\n",
    "    username = input(\"Enter Username: \")\n",
    "\n",
    "    if username not in users:\n",
    "        print(\"User not found\\n\")\n",
    "        return\n",
    "\n",
    "    old_password = getpass.getpass(\"Enter Old Password: \")\n",
    "\n",
    "    if users[username] == old_password:\n",
    "        new_password = getpass.getpass(\"Enter New Password: \")\n",
    "\n",
    "        if check_password_strength(new_password):\n",
    "            users[username] = new_password\n",
    "            print(\"Password Reset Successfully\\n\")\n",
    "        else:\n",
    "            print(\"Weak Password\")\n",
    "\n",
    "    else:\n",
    "        print(\"Old password is incorrect!\")\n",
    "\n",
    "#Main menu\n",
    "while True:\n",
    "    print(\"\\n-------Main Menu-------\\n\")\n",
    "    print(\"1.Register\")\n",
    "    print(\"2.Login\")\n",
    "    print(\"3.Reset Password\")\n",
    "    print(\"4.Exit\")\n",
    "\n",
    "    choice = input(\"Enter your choice: \")\n",
    "\n",
    "    if choice == \"1\":\n",
    "        register()\n",
    "    elif choice == \"2\":\n",
    "        login()\n",
    "    elif choice == \"3\":\n",
    "        reset_password()\n",
    "    elif choice == \"4\":\n",
    "        print(\"Exiting Program!\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Invalid Choice!\")\n",
    "    \n",
    "\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9219787b-9629-4261-897e-cb6e24fa54f0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

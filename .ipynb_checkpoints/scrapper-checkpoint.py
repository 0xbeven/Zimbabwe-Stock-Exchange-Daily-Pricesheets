{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "ename": "GitCommandError",
     "evalue": "Cmd('git') failed due to: exit code(128)\n  cmdline: git push\n  stderr: 'fatal: could not read Username for 'https://github.com': No such device or address'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mGitCommandError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-48-41eaa8e3a210>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     49\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     50\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"__main__\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 51\u001b[0;31m     \u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     52\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-48-41eaa8e3a210>\u001b[0m in \u001b[0;36mmain\u001b[0;34m()\u001b[0m\n\u001b[1;32m     44\u001b[0m     \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_todays_pricesheet\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mURL\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     45\u001b[0m     \u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto_excel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mset_todays_filename\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheader\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mindex\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 46\u001b[0;31m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mupdate_repo\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     47\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     48\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-48-41eaa8e3a210>\u001b[0m in \u001b[0;36mupdate_repo\u001b[0;34m()\u001b[0m\n\u001b[1;32m     37\u001b[0m     \u001b[0mrepo\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"--all\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m     \u001b[0mrepo\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'-m created new file {set_todays_filename()}'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 39\u001b[0;31m     \u001b[0mrepo\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpush\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     40\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mrepo\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     41\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/git/cmd.py\u001b[0m in \u001b[0;36m<lambda>\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    540\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'_'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    541\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mLazyMixin\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__getattr__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 542\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0;32mlambda\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_call_process\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    543\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    544\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mset_persistent_git_options\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/git/cmd.py\u001b[0m in \u001b[0;36m_call_process\u001b[0;34m(self, method, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1003\u001b[0m         \u001b[0mcall\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mextend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1004\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1005\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcall\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mexec_kwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1006\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1007\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_parse_object_header\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheader_line\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.8/dist-packages/git/cmd.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, command, istream, with_extended_output, with_exceptions, as_process, output_stream, stdout_as_string, kill_after_timeout, with_stdout, universal_newlines, shell, env, max_chunk_size, **subprocess_kwargs)\u001b[0m\n\u001b[1;32m    820\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    821\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mwith_exceptions\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mstatus\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 822\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mGitCommandError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstatus\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstderr_value\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstdout_value\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    823\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    824\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstdout_value\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbytes\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mstdout_as_string\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# could also be output_stream\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mGitCommandError\u001b[0m: Cmd('git') failed due to: exit code(128)\n  cmdline: git push\n  stderr: 'fatal: could not read Username for 'https://github.com': No such device or address'"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from datetime import date\n",
    "import pandas as pd\n",
    "import git\n",
    "\n",
    "URL = \"https://www.zse.co.zw/price-sheet/\"\n",
    "# REPO_URL = \"https://github.com/bevennyamande/Scrapper.git\"\n",
    "\n",
    "def get_todays_pricesheet(URL: str):\n",
    "    \"\"\" Get the price sheet from the website \"\"\"\n",
    "    \n",
    "    dataframe = pd.read_html(URL)\n",
    "    return dataframe\n",
    "\n",
    "\n",
    "def get_todays_date() -> str:\n",
    "    \"\"\" Get todays date \"\"\"\n",
    "    \n",
    "    today_date = date.today()\n",
    "    return today_date.strftime(\"%d-%m-%Y\") # dd-mm-YY\n",
    "\n",
    "\n",
    "def set_todays_filename() ->str:\n",
    "    \"\"\" Name to save the excel file \"\"\"\n",
    "    \n",
    "    return f'{get_todays_date()}.xlsx'\n",
    "\n",
    "\n",
    "def is_file_exist():\n",
    "    \"\"\" Check if the file already exists \"\"\"\n",
    "    pass\n",
    "\n",
    "\n",
    "# def update_repo():\n",
    "#     repo = git.Repo(\"\")\n",
    "#     repo.init()\n",
    "#     repo.git.add(\"--all\")\n",
    "#     repo.git.commit(f'-m created new file {set_todays_filename()}')\n",
    "#     repo.git.push()\n",
    "#     return repo\n",
    "\n",
    "\n",
    "def main():\n",
    "    df = get_todays_pricesheet(URL)\n",
    "    df[0].to_excel(set_todays_filename(), header=True, index=False)\n",
    "#     print(update_repo())\n",
    "    \n",
    "    \n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

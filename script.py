#/usr/bin/python3

import os
import argparse
import requests as rq
GIT_API_URL = 'https://api.github.com'
GIT_CLONE_DIRECTORY = '<diectory_path>' # ~/opt/project/


class Clone(object):

    def __init__(self, *args, **kwargs):
        self.username = args[0] if len(args) > 0 else ''
        self.reponame = args[1] if len(args) > 1 else ''

    def run(self, *args, **kwargs):
        final_path = '{}{}'.format(GIT_CLONE_DIRECTORY, self.username)
        if not os.path.exists(final_path):
            os.makedirs(final_path)
            os.chmod(final_path, 755)

        if self.reponame:
            url = '{}/repos/{}/{}'.format(GIT_API_URL, self.username, self.reponame)
        else:
            url = '{}/users/{}/repos'.format(GIT_API_URL, self.username)
        __get_object = rq.get(url=url)
        if __get_object.status_code == 200:
            if isinstance(__get_object.json(), list):
                for rp in __get_object.json():
                    self.clone(rp['clone_url'], final_path)
            if isinstance(__get_object.json(), dict):
                rp = __get_object.json()
                self.clone(rp['clone_url'], final_path)
        else:
            print(__get_object.status_code)
            print(__get_object.text)

    def clone(self, url, path, *args, **kwargs):
        cmd = 'git clone {}'.format(url)
        os.chdir(path)
        os.system(cmd)

    def stop(self, *args, **kwargs):
        pass


def clone(username, reponame=None):
    c = Clone(username, reponame)
    c.run()


if __name__ == '__main__':
    # initiate the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", "-u", help="show username version", required=True)
    parser.add_argument("--reponame", "-r", help="show reponame version", required=False)

    # read arguments from the command line
    args = parser.parse_args()

    # check for --version or -V
    u_name = None
    r_name = None
    if args.username:
        print("this is username {} ".format(args.username))
        u_name = args.username
    if args.reponame:
        r_name = args.reponame
        print("this is reponame {} ".format(args.reponame))
    clone(username=u_name, reponame=r_name)

#!/usr/bin/env python2.7

import unittest
from photos.photo_manager.users import *

class TestUser(unittest.TestCase):
    def setup(self):
        pass

    def test_create_user_object(self):
        uname='testuser1'
        password = 'testpass1'
        email='test@test.com'
        user = User(uname, password, email)
        self.assertEqual(uname, user.username)
        self.assertNotEqual(None, user.last_login_time)


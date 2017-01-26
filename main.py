#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def build_page(content):
	header = "<h1>Web Caeser</h1>"
	rot_input = "<label>Enter Rotation</label><br /><input type='number'/ name = 'rot'><br /><br />"
	textarea = "<label>Enter Text</label><br /><textarea name = 'message'>" + content + "</textarea><br /><br />"
	input = textarea + "<input type = 'submit'/>"
	form = header + "<form method = 'post'>" + rot_input + input + "</form>"
	return(form)
	
class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(build_page(""))
		
	def post(self):
		message = self.request.get("message")
		rot = int(self.request.get("rot"))
		encrypted_message = caesar.encrypt(message, rot)
		sanitized_message = cgi.escape(encrypted_message)
		self.response.write(build_page(sanitized_message))

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)

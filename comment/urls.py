#coding: utf-8
#This file is part of Ficlatté.
#Copyright © 2015-2017 Paul Robertson, Jim Stitzel and Shu Sam Chen
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of version 3 of the GNU Affero General Public
#    License as published by the Free Software Foundation
#
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^submit/$', 'comment.views.submit_comment', name='submit_comment'),
    url(r'^(?P<comment_id>\d+)/like/$', 'comment.views.like_comment', name='like_comment'),
    url(r'^(?P<comment_id>\d+)/unlike/$', 'comment.views.unlike_comment', name='unlike_comment'),
]

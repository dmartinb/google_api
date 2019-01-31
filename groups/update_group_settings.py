#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pprint
import sys
import json

from googleapiclient.discovery import build
from google.oauth2 import service_account

DEBUG = True
# DEBUG = False

# Console <http://code.google.com/apis/console>
SCOPES = ['https://www.googleapis.com/auth/apps.groups.settings']
CONFIG_FILE='private/config.json'


def load_config(file):
  """ config from json file

  """
  with open(file) as f:
    data = json.load(f)
  return data


def update_settings(service, groupId, settings):
  """ update group settings

  Args:
    service: API service object.
    groupId: group@domain identifier.
    settings: group settings.
  """

  groups = service.groups()
  g = groups.get(groupUniqueId=groupId).execute()

  body = {}

  # Extract the properties and add to dictionary body.
  for key, val in settings.items():
    if key is not None:
      body[key] = val

  if not body:
    if DEBUG: print('\nEmpty settings')
    return

  # Update
  g1 = groups.update(groupUniqueId=groupId, body=body).execute()

  print('\nUpdated')
  if DEBUG: pprint.pprint(g)


def main(argv):
  """MAIN - Groups Settings API."""

  if DEBUG: print('\nLoad config')
  config = load_config(CONFIG_FILE)
  if DEBUG:
    print('\nSettings')
    pprint.pprint(config['settings'])

  # service account access (machine-machine)
  credentials = service_account.Credentials.from_service_account_file(
    config['service_account_file'],
    scopes=SCOPES)
  # credential - on behalf of...
  delegated_credentials = credentials.with_subject(config['userid'])

  service = build('groupssettings', 'v1', credentials=delegated_credentials)
  update_settings(service=service, groupId=config['groupid'],
    settings=config['settings'])

if __name__ == '__main__':
  main(sys.argv)

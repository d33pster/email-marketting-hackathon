#!/usr/bin/env python3

from mailchimp3 import MailChimp
from string import Template
from pandas import DataFrame

class _mailchimp:
    def __init__(self):
        self._api_key = ''
        self._username = ''
        self._emaillist = []
        self._audience_creation_dictionary = {}
    
    def _set_client(self):
        self._client = MailChimp(mc_api=self._api_key, mc_user=self._username)
        
    def _createAudience(self):
        self._audience = ''
        aude_list = {
            'name': self._audience_creation_dictionary['name'],
            'contact': {
                'company': self._audience_creation_dictionary['company'],
                'address': self._audience_creation_dictionary['address'],
                'city': self._audience_creation_dictionary['city'],
                'state': self._audience_creation_dictionary['state'],
                'zip': self._audience_creation_dictionary['zip'],
                'country': self._audience_creation_dictionary['country']
            },
            'permission_reminder': self._audience_creation_dictionary['name'],
            'campaign_defaults': {
                'from_name': self._audience_creation_dictionary['from_name'],
                'from_email': self._audience_creation_dictionary['from_email'],
                'subject': "",
                'language': self._audience_creation_dictionary['language']
            },
            'email_type_option': False
        }
        
        try:
            self._audience = self._client.lists.create(data=aude_list)
        except Exception as error:
            self._audience_creation_errorText = error
    
    def _add_members(self):
        if len(self._emaillist)!=0:
            for email in self._emaillist:
                try:
                    data = {
                        'status':'subscribed',
                        'email_address':email
                    }
                    
                    self._client.lists.members.create(list_id=self._audience['id'], data=data)
                except Exception as error:
                    self._add_members_errorText = error
        else:
            self._add_members_errorText = "Mailing List is empty."
    
    def _create_campaign(self, _name, _reply_to):
        data = {
            'recipients': {
                'list_id':int(self._audience['id'])
            },
            'settings':{
                'subject_line': _name,
                'from_name': self._audience_creation_dictionary['from_name'],
                'reply_to': _reply_to
            },
            'type': 'regular'
        }
        
        self._campaign = self._client.campaigns.create(data=data)
    
    def _send(self):
        try:
            self._client.campaigns.actions.send(campaign_id=self._campaign['id'])
        except Exception as error:
            self._mailError = error
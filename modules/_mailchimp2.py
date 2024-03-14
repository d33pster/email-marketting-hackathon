#!/usr/bin/env python3

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

class mailchimp:
    def __init__(self):
        self._api_key = ''
        self._server = ''
        self._audience_dict = {}
        self._campaign_dict = {}
        self._emaillist = []
        self._audience = ''
    
    def _setClient(self):
        self._mailchimp = MailchimpMarketing.Client()
        self._mailchimp.set_config({
            "api_key":self._api_key,
            "server":self._server
        })
    
    def _makeAudienceList(self):
        try:
            self._audience = self._mailchimp.lists.create_list(body={
                "name":self._audience_dict['aud_name'],
                "contact": {
                    "company":self._audience_dict['company'],
                    "address1":self._audience_dict['address'],
                    "address2": "",
                    "city":self._audience_dict['city'],
                    "state":self._audience_dict['state'],
                    "zip":self._audience_dict['zip'],
                    "country":self._audience_dict['country'],
                    "Phone": ""
                },
                "permission_reminder": "You'receiving this email because you signed up.",
                "campaign_defaults":{
                    "from_name":self._audience_dict['from_name'],
                    "from_email":self._audience_dict['from_email'],
                    "subject":self._campaign_dict['subject'],
                    "language":"en"
                },
                "email_type_option":True
            })
        except ApiClientError as error:
            print(f"MAILCHIMP AUDIENCE ERROR: {error.text}")
    
    def _addEmails(self):
        try:
            audiences = self._mailchimp.lists.get_all_lists()
            for audience in audiences['lists']:
                if audience['name'] == self._audience_dict['aud_name']:
                    self._audid = audience['id']
            self._addemailresponse = self._mailchimp.lists.batch_list_members(self._audid,{
                "members": self._emaillist,
                "update_existing":True
            })
        except ApiClientError as error:
            print(f"MAILCHIMP EMAIL ERROR: {error.text}")
    
    def _create_campaign(self):
        try:
            self._campaign = self._mailchimp.campaigns.create(body={
                "type": "regular",
                "recipients":{
                    "list_id":self._audid
                },
                "settings":{
                    "subject_line":self._campaign_dict['subject'],
                    "title": self._audience_dict['aud_name'].split('_')[0],
                    "from_name": self._audience_dict['from_name'],
                    "reply_to": self._audience_dict['from_email']
                }
            })
        except ApiClientError as error:
            print(f"MAILCHIMP CAMPAIGN ERROR: {error.text}")
    
    def _sendCampaign(self, time):
        try:
            self._sendResponse = self._mailchimp.campaigns.schedule(self._campaign['id'], {"schedule_time":time})
        except ApiClientError as error:
            print(f"MAILCHIMP ERROR: {error.text}")
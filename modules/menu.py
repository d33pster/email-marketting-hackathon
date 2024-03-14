#!/usr/bin/env python3

# code for initial screen
from tkinter import *
from tkinter import ttk
from modules._List import _list
from modules._mailchimp2 import mailchimp
import pandas as pd
from os.path import exists as there
from os import remove
from tkcalendar import Calendar
from datetime import datetime
from platform import system as getos

class generate:
    def __init__(self, master: Tk, title: str):
        self._os = getos()
        self.parent = master
        # title
        self._title = title
        self.parent.title(self._title)
        # set geometry
        self.parent.geometry('600x450+580+290')
        # create an enclosing frame
        self._EnclosingFrame = ttk.Frame(self.parent)
        self._EnclosingFrame.pack(fill=BOTH, expand=True)
        
        self._style = ttk.Style()
        
        # create data for mailing list
        self._treeheaders = []
        self._treedata = []
        self._dataframe = pd.DataFrame(columns=['Serial No.', 'Name', 'Email', 'Address', 'Phone'])
        if there("_mailinglist_.csv"):
            self._dataframe = pd.read_csv('_mailinglist_.csv')
            for col in self._dataframe.columns:
                self._treeheaders.append(col)
            for index in self._dataframe.index:
                self._treedata.append(tuple((self._dataframe['Serial No.'][index], self._dataframe['Name'][index], self._dataframe['Email'][index], self._dataframe['Address'][index], self._dataframe['Phone'][index])))
        
        # create data for campaigns
        self._campaignTreeHeaders = []
        self._campaignTreeData = []
        self._campaignDataFrame = pd.DataFrame(columns=['ID', 'Campaigns'])
        if there("_campaignlist_.csv"):
            self._campaignDataFrame = pd.read_csv("_campaignlist_.csv")
            for col in self._campaignDataFrame.columns:
                self._campaignTreeHeaders.append(col)
            for index in self._campaignDataFrame.index:
                self._campaignTreeData.append(tuple((self._campaignDataFrame['ID'][index], self._campaignDataFrame['Campaigns'][index])))
        
        # create mailchimp object
        self._mailchimp = mailchimp()
    
    def _reinitialize(self):
        for widget in self._EnclosingFrame.winfo_children():
            widget.destroy()
        self._style = ttk.Style()
        
        # create class data set
        self._treeheaders = []
        self._treedata = []
        self._dataframe = pd.DataFrame(columns=['Serial No.', 'Name', 'Email', 'Address', 'Phone'])
        if there("_mailinglist_.csv"):
            self._dataframe = pd.read_csv('_mailinglist_.csv')
            for col in self._dataframe.columns:
                self._treeheaders.append(col)
            for index in self._dataframe.index:
                self._treedata.append(tuple((self._dataframe['Serial No.'][index], self._dataframe['Name'][index], self._dataframe['Email'][index], self._dataframe['Address'][index], self._dataframe['Phone'][index])))

        # create data for campaigns
        self._campaignTreeHeaders = []
        self._campaignTreeData = []
        self._campaignDataFrame = pd.DataFrame(columns=['ID', 'Campaigns'])
        if there("_campaignlist_.csv"):
            self._campaignDataFrame = pd.read_csv("_campaignlist_.csv")
            for col in self._campaignDataFrame.columns:
                self._campaignTreeHeaders.append(col)
            for index in self._campaignDataFrame.index:
                self._campaignTreeData.append(tuple((self._campaignDataFrame['ID'][index], self._campaignDataFrame['Campaigns'][index])))
        
        # create mailchimp object
        self._mailchimp = mailchimp()
    
    def _destroy(self):
        self.parent.destroy()
    
    def _menu(self):
        # create a notebook for menu windows
        self._notebook = ttk.Notebook(self._EnclosingFrame)
        self._notebook.pack(expand=True, fill=BOTH)
        
        # create frames for tabs
        self._MailingList = ttk.Frame(self._notebook)
        self._Campaigns = ttk.Frame(self._notebook)
        self._Schedule = ttk.Frame(self._notebook)
        self._Performance = ttk.Frame(self._notebook)
        
        # add them in notebook
        self._notebook.add(self._Campaigns, text='Campaigns')
        self._notebook.add(self._MailingList, text='Mailing List')
        self._notebook.add(self._Schedule, text='Schedule')
        self._notebook.add(self._Performance, text='Performance')
        
        ### Mailing List ###
        self._MLEnclosingFrame = ttk.Frame(self._MailingList)
        self._MLEnclosingFrame.pack(fill=BOTH, expand=True)
        
        # show mailing list and add an edit button
        if len(self._treedata) == 0:
            self._MLErrorFrame = ttk.Frame(self._MLEnclosingFrame)
            self._MLErrorFrame.pack(expand=True, fill=BOTH)
            self._MLErrorLabel = ttk.Label(self._MLErrorFrame, text='NO DATA.')
            self._MLErrorLabel.place(relx=0.5, rely=0.5, anchor='center')
        else:
            self._makeMailingList(self._MLEnclosingFrame)
        
        # create a frame for add button and delete button
        self._mailingButtonFrame = ttk.Frame(self._MLEnclosingFrame)
        self._mailingButtonFrame.pack(fill=BOTH)
        self._mailingListAddButton = ttk.Button(self._mailingButtonFrame, text='add', default='active', command=self._mailingListAddButton_)
        self._mailingListAddButton.pack(side=LEFT)
        self._mailingListDeleteButton = ttk.Button(self._mailingButtonFrame, text='delete', command=self._mailingListDeleteButton_)
        self._mailingListDeleteButton.pack(side=RIGHT)
        ### Mailing List END ###
        
        ### Campaign ###
        self._campaignEnclosingFrame = ttk.Frame(self._Campaigns)
        self._campaignEnclosingFrame.pack(fill=BOTH, expand=True)
        
        # add a separator for list of campaigns
        self._campaignSeparator = ttk.Separator(self._campaignEnclosingFrame, orient='vertical')
        self._campaignSeparator.place(relx=0.24, rely=0, relwidth=0.2, relheight=1)
        
        # add a frame on both sides of the separators
        self._campaignLeftEnclosingFrame = ttk.Frame(self._campaignEnclosingFrame)
        self._campaignLeftEnclosingFrame.place(relx=0, rely=0, relheight=1, relwidth=0.33)
        
        self._campaignRightEnclosingFrame = ttk.Frame(self._campaignEnclosingFrame)
        self._campaignRightEnclosingFrame.place(relx=0.35, rely=0, relheight=1, relwidth=0.65)
        
        # create another frame with pack method for positional reasons
        self._campaignLeftFrame = ttk.Frame(self._campaignLeftEnclosingFrame)
        self._campaignLeftFrame.pack(fill=BOTH, expand=True)
        self._campaignRightFrame = ttk.Frame(self._campaignRightEnclosingFrame)
        self._campaignRightFrame.pack(fill=BOTH, expand=True)
        
        # add a list of created campaigns to the left side
        if len(self._campaignTreeData) == 0:
            self._campaignErrorFrame = ttk.Frame(self._campaignLeftFrame)
            self._campaignErrorFrame.pack(fill=BOTH, expand=True)
            self._campaignErrorLabel = ttk.Label(self._campaignErrorFrame, text="NO DATA.")
            self._campaignErrorLabel.place(relx=0.5, rely=0.5, anchor='center')      
        else:
            self._makeCampaignList(self._campaignLeftFrame)
        
        # on the right frame make form to enter campaign details
        self._campaignLabel = ttk.Label(self._campaignRightFrame, text='Create Campaign', font='Helvetica 13 bold')
        self._campaignLabel.place(relx=0.5, rely=0.02, anchor='center')
        # enter campaign name:
        self._campaigNameLabel = ttk.Label(self._campaignRightFrame, text='Campaign Name:')
        self._campaigNameLabel.place(relx=0.23, rely=0.14, anchor='center')
        self._campaigNameEntry = ttk.Entry(self._campaignRightFrame, width=20)
        self._campaigNameEntry.place(relx=0.65, rely=0.14, anchor='center')
        # campaign subject name:
        self._campaignSubjectLabel = ttk.Label(self._campaignRightFrame, text='Subject:')
        self._campaignSubjectLabel.place(relx=0.23, rely=0.2, anchor='center')
        self._campaignSubjectEntry = ttk.Entry(self._campaignRightFrame, width=20)
        self._campaignSubjectEntry.place(relx=0.65, rely=0.2, anchor="center")
        
        # a label for company details
        self._CompanyLabel = ttk.Label(self._campaignRightFrame, text='Company Details', font='Helvetica 11 bold')
        self._CompanyLabel.place(relx=0.5, rely=0.30, anchor='center')
        # enter company name
        self._companyNameLabel = ttk.Label(self._campaignRightFrame, text='Company name:')
        self._companyNameLabel.place(relx=0.23, rely=0.38, anchor='center')
        self._companyNameEntry = ttk.Entry(self._campaignRightFrame, width=20)
        self._companyNameEntry.place(relx=0.65, rely=0.38, anchor='center')
        # enter Company Address
        self._companyAddressLabel = ttk.Label(self._campaignRightFrame, text='Company Address:')
        self._companyAddressLabel.place(relx=0.23, rely=0.45, anchor='center')
        self._companyAddressEntry = ttk.Entry(self._campaignRightFrame, width=20)
        self._companyAddressEntry.place(relx=0.67, rely=0.45, anchor='center')
        # enter company city and state
        self._companyCityLabel = ttk.Label(self._campaignRightFrame, text='City:')
        self._companyCityLabel.place(relx=0.08, rely=0.52, anchor='center')
        self._companyCityEntry = ttk.Entry(self._campaignRightFrame, width=12)
        self._companyCityEntry.place(relx=0.3, rely=0.52, anchor='center')
        self._companyStateLabel = ttk.Label(self._campaignRightFrame, text='State:')
        self._companyStateLabel.place(relx=0.52, rely=0.52, anchor='center')
        self._companyStateEntry = ttk.Entry(self._campaignRightFrame, width=12)
        self._companyStateEntry.place(relx=0.75, rely=0.52, anchor='center')
        # enter country and zipcode
        self._companyCountryLabel = ttk.Label(self._campaignRightFrame, text='Country:')
        self._companyCountryLabel.place(relx=0.10, rely=0.59, anchor='center')
        self._companyCountryEntry = ttk.Entry(self._campaignRightFrame, width=11)
        self._companyCountryEntry.place(relx=0.33, rely=0.59, anchor='center')
        self._companyZipLabel = ttk.Label(self._campaignRightFrame, text='Zip code:')
        self._companyZipLabel.place(relx=0.57, rely=0.59, anchor='center')
        self._companyZipEntry = ttk.Entry(self._campaignRightFrame, width=9)
        self._companyZipEntry.place(relx=0.79, rely=0.59, anchor='center')
        # give a check box to save the company details for next time
        # self._saveCompanyDetailsCB_choice = BooleanVar()
        # self._saveCompanyDetailsCB = ttk.Checkbutton(self._campaignRightFrame, variable=self._saveCompanyDetailsCB_choice,  text='Save company details for future', onvalue=True, offvalue=False)
        # self._saveCompanyDetailsCB.place(relx=0.5, rely=0.62, anchor='center')
        
        # a label for other details
        self._otherLabel = ttk.Label(self._campaignRightFrame, text='Other Details', font='Helvetica 11 bold')
        self._otherLabel.place(relx=0.5, rely=0.71, anchor='center')
        # enter from name
        self._fromNameLabel = ttk.Label(self._campaignRightFrame, text='From (name):')
        self._fromNameLabel.place(relx=0.26, rely=0.78, anchor='center')
        self._fromNameEntry = ttk.Entry(self._campaignRightFrame, width=20)
        self._fromNameEntry.place(relx=0.65, rely=0.78, anchor='center')
        # enter from email
        self._fromEmailLabel = ttk.Label(self._campaignRightFrame, text='From (email):')
        self._fromEmailLabel.place(relx=0.26, rely=0.85, anchor='center')
        self._fromEmailEntry = ttk.Entry(self._campaignRightFrame, width=20)
        self._fromEmailEntry.place(relx=0.65, rely=0.85, anchor='center')
        # end of entry #

        # button frame
        self._campaignRightButtonFrame = ttk.Frame(self._campaignRightEnclosingFrame)
        self._campaignRightButtonFrame.pack(fill=BOTH)
        # create Add Button and delete button
        self._campaignAddButton = ttk.Button(self._campaignRightButtonFrame, text='add', default='active', command=self._campaignAddButton_)
        self._campaignAddButton.pack(side=LEFT)
        self._campaignDeleteButton = ttk.Button(self._campaignRightButtonFrame, text='delete', command=self._campaignDeleteButton_)
        self._campaignDeleteButton.pack(side=RIGHT)
        ### campaign END ###
        
        ### Schedule ###
        self._scheduleEnclosingFrame = ttk.Frame(self._Schedule)
        self._scheduleEnclosingFrame.pack(fill=BOTH, expand=True)
        
        # create another frame to fill
        self._scheduleFirstFrame = ttk.Frame(self._scheduleEnclosingFrame)
        self._scheduleFirstFrame.pack(fill=BOTH, expand=True)
        
        # choose a campaign
        self._campaign = StringVar()
        self._campaigns = self._campaignDataFrame['Campaigns'].to_list()
        self._dropdown = ttk.OptionMenu(self._scheduleFirstFrame, self._campaign, 'No Campaign Selected', *self._campaigns)
        self._dropdown.place(relx=0.4, rely=0.1, anchor='center', relwidth=0.7)
        
        # create a date selector
        self._schedule_label = ttk.Label(self._scheduleFirstFrame, text='Select Date:')
        self._schedule_label.place(relx=0.13, rely=0.25, anchor='center')
        self._calendar = Calendar(self._scheduleFirstFrame, selectmode='day', year=2024, month=3, day=4, bordercolor='black', selectforeground='red', foreground='black', background='white')
        self._calendar.place(relx=0.25, rely=0.5, anchor='center')
        
        # create time selector        
        # month
        self._hour = StringVar()
        self._hours = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23', '24'
        ]
        self._hourDropdown = ttk.OptionMenu(self._scheduleFirstFrame, self._hour, 'Select Hour', *self._hours)
        self._hourDropdown.place(relx=0.17, rely=0.8, anchor='center', relwidth=0.3)
        
        self._minute = StringVar()
        self._minutes = [
            '00', '15', '30', '45', '60'
        ]
        self._minuteDropdown = ttk.OptionMenu(self._scheduleFirstFrame, self._minute, 'Select Minutes', *self._minutes)
        self._minuteDropdown.place(relx=0.5, rely=0.8, anchor='center', relwidth=0.3)
        
        # create a button frame
        self._scheduleButtonFrame = ttk.Frame(self._scheduleEnclosingFrame)
        self._scheduleButtonFrame.pack(fill=BOTH)
        # create buttons
        self._scheduleButton = ttk.Button(self._scheduleButtonFrame, text='Schedule', command=self._schedule_, default='active')
        self._scheduleButton.pack(side=RIGHT)
        ### schedule END ###
    
    def _schedule_(self):
        # get date
        schedule_date = self._calendar.get_date().split('/')
        self._schedule_month = schedule_date[0]
        self._schedule_day = schedule_date[1]
        self._schedule_year = schedule_date[2]
        # create a popup
        self._topMailchimpWindow = Toplevel(self.parent)
        self._topMailchimpWindow.title(self._title+" Credentials")
        self._topMailchimpWindow.geometry('600x200+690+400')
        # create a notebook
        self._topMailchimpWindow_notebook = ttk.Notebook(self._topMailchimpWindow)
        self._topMailchimpWindow_notebook.pack(fill=BOTH, expand=True)
        # create tab frames
        self._topMailchimpWindow_notebook_mailchimp = ttk.Frame(self._topMailchimpWindow_notebook)
        self._topMailchimpWindow_notebook_comingsoon = ttk.Frame(self._topMailchimpWindow_notebook)
        # add the tabs
        self._topMailchimpWindow_notebook.add(self._topMailchimpWindow_notebook_mailchimp, text='Mailchimp')
        self._topMailchimpWindow_notebook.add(self._topMailchimpWindow_notebook_comingsoon, text='Coming Soon')
        # set comingsoon tab disabled
        self._topMailchimpWindow_notebook.tab(1, state='disabled')
        
        # create an enclosing frame under mailchimp
        self._top_mailchimp_EnclosingFrame = ttk.Frame(self._topMailchimpWindow_notebook_mailchimp)
        self._top_mailchimp_EnclosingFrame.pack(fill=BOTH, expand=True)
        ## define mailchimp tab
        # add label
        self._top_mailchimp_apiLabel = ttk.Label(self._top_mailchimp_EnclosingFrame, text='API Key:')
        self._top_mailchimp_apiLabel.place(relx=0.32, rely=0.3, anchor='center')
        # add entry
        self._top_mailchimp_apiEntry = ttk.Entry(self._top_mailchimp_EnclosingFrame, width=25)
        self._top_mailchimp_apiEntry.place(relx=0.59, rely=0.3, anchor='center')
        # add server label
        self._top_mailchimp_serverLabel = ttk.Label(self._top_mailchimp_EnclosingFrame, text='server:')
        self._top_mailchimp_serverLabel.place(relx=0.32, rely=0.51, anchor='center')
        # add server entry
        self._top_mailchimp_serverEntry = ttk.Entry(self._top_mailchimp_EnclosingFrame, width=25)
        self._top_mailchimp_serverEntry.place(relx=0.59, rely=0.51, anchor='center')
        
        # create a button frame
        self._top_buttonFrame = ttk.Frame(self._topMailchimpWindow_notebook_mailchimp)
        self._top_buttonFrame.pack(fill=BOTH)
        # create Submit button
        self._top_submit = ttk.Button(self._top_buttonFrame, text='submit', default='active', command=self._top_submit_)
        self._top_submit.pack(side='top')
        
        self._topMailchimpWindow.mainloop()
    
    def _top_submit_(self):
        # set username and api key
        self._mailchimp._api_key = self._top_mailchimp_apiEntry.get().strip()
        self._mailchimp._server = self._top_mailchimp_serverEntry.get().strip()
        self._topMailchimpWindow.destroy()
        # setup audience dictionary
        with open(f'_companydeets_{self._campaign.get()}_.data', 'r') as f:
            companydeets = f.readlines()
        
        for line in companydeets:
            line = line.replace("\n", "")
            if line.split(':')[0]=='company':
                self._mailchimp._audience_dict['company'] = line.split(':')[1]
                # self._mailchimp._audience_dict['aud_name'] = line.split(':')[1] + "_audience"
            elif line.split(':')[0]=='address':
                self._mailchimp._audience_dict['address'] = line.split(':')[1]
            elif line.split(":")[0]=='subject':
                self._mailchimp._campaign_dict['subject'] = line.split(":")[1]
            elif line.split(":")[0]=='campaign':
                self._mailchimp._audience_dict['aud_name'] = line.split(":")[1]
            elif line.split(':')[0]=='city':
                self._mailchimp._audience_dict['city'] = line.split(':')[1]
            elif line.split(':')[0]=='state':
                self._mailchimp._audience_dict['state'] = line.split(':')[1]
            elif line.split(':')[0]=='country':
                self._mailchimp._audience_dict['country'] = line.split(':')[1]
            elif line.split(':')[0]=='zip':
                self._mailchimp._audience_dict['zip'] = line.split(':')[1]
            elif line.split(':')[0]=='from_name':
                self._mailchimp._audience_dict['from_name'] = line.split(':')[1]
            elif line.split(':')[0]=='from_email':
                self._mailchimp._audience_dict['from_email'] = line.split(':')[1]
        
        # setup client
        self._mailchimp._setClient()
        # create audience
        self._mailchimp._makeAudienceList()
        # set email list
        # self._mailchimp._emaillist = self._dataframe['Email'].to_list()
        datalist = []
        for item in self._dataframe['Email'].to_list():
            data = {
                "email_address":item,
                "status": "subscribed"
            }
            datalist.append(data)
        
        print(datalist)
        
        self._mailchimp._emaillist = datalist
        # add members
        self._mailchimp._addEmails()
        
        # make campaign dict
        
        # create campaign
        self._mailchimp._create_campaign()
        
        # create a scheduler process
        # def scheduler(day: int, month: int, year: int):
        #     if len(str(day))==1:
        #         day = "0"+str(day)
        #     if len(str(month))==1:
        #         month = "0"+str(month)
        #     while(True):
        #         if datetime.today()==f"{year}-{month}-{day}":
        #             if datetime.now().strftime("%H:%M") == "07:00":
        #                 self._mailchimp._send()
        
        
        # start this for the current campaign
        # process = multiprocessing.Process(target=scheduler, args=(self._schedule_day, self._schedule_month, self._schedule_year))
        # process.start()
        ###### using crontab
        # if self._os != 'Windows':
        
        self._mailchimp._sendCampaign(time=f"{self._schedule_year}-{self._schedule_month}-{self._schedule_day}T{self._hour}:{self._minute}:00")
            
        
    
    def _campaignDeleteButton_(self):
        # create an popup window
        self._topDeleteWindow = Toplevel(self.parent)
        self._topDeleteWindow.title(self._title+" -> Delete Entry")
        self._topDeleteWindow.geometry('300x65+718+490')
        
        # create an enclosing frame
        self._topDeleteWindow_EnclosingFrame = ttk.Frame(self._topDeleteWindow)
        self._topDeleteWindow_EnclosingFrame.pack(fill=BOTH, expand=True)
        
        # create frame for text fields
        self._topDeleteWindow_EnclosingFrame_FirstFrame = ttk.Frame(self._topDeleteWindow_EnclosingFrame)
        self._topDeleteWindow_EnclosingFrame_FirstFrame.pack(fill=BOTH, expand=True)
        
        self._topDeleteWindow_EnterSerialLabel = ttk.Label(self._topDeleteWindow_EnclosingFrame_FirstFrame, text='ID:')
        self._topDeleteWindow_EnterSerialLabel.place(relx=0.4, rely=0.2, anchor="center")
        self._topDeleteWindow_EnterSerialEntry = ttk.Entry(self._topDeleteWindow_EnclosingFrame_FirstFrame, width=8)
        self._topDeleteWindow_EnterSerialEntry.place(relx=0.6, rely=0.2, anchor='center')
        
        # create another frame for buttons
        self._topDeleteWindow_ButtonFrame = ttk.Frame(self._topDeleteWindow_EnclosingFrame)
        self._topDeleteWindow_ButtonFrame.pack(fill=BOTH)
        
        # add buttons
        self._topDeleteWindow_DeleteButton = ttk.Button(self._topDeleteWindow_ButtonFrame, text='delete', command=self._toplevelDelete_Campaign_)
        self._topDeleteWindow_DeleteButton.pack(side=LEFT)
        self._topDeleteWindow_BackButton = ttk.Button(self._topDeleteWindow_ButtonFrame, text='back', command=self._toplevelBackButton_Campaign_)
        self._topDeleteWindow_BackButton.pack(side=RIGHT)
        
        self._topDeleteWindow.mainloop()
    
    def _toplevelDelete_Campaign_(self):
        ID = int(self._topDeleteWindow_EnterSerialEntry.get().strip())
        self._topDeleteWindow.destroy()
        
        campaignName = self._campaignDataFrame['Campaigns'][ID-1]
        remove(f"_companydeets_{campaignName}_.data")
        
        self._campaignDataFrame.drop(ID-1, axis=0, inplace=True)
        self._campaignDataFrame.loc[self._campaignDataFrame['ID']>ID-1, 'ID'] -= 1
        
        self._campaignDataFrame.to_csv('_campaignlist_.csv', index=False)
        self._reinitialize()
        self._menu()
        self._notebook.select(0)
    
    def _toplevelBackButton_Campaign_(self):
        self._topDeleteWindow.destroy()
    
    def _campaignAddButton_(self):
        # save campaign list
        data = {
            'ID':len(self._campaignTreeData)+1,
            'Campaigns':self._campaigNameEntry.get().strip()
        }
        if self._os=='Windows':
            self._campaignDataFrame = self._campaignDataFrame.append(data, ignore_index=True)
        else:
            self._campaignDataFrame = self._campaignDataFrame._append(data, ignore_index=True)
        
        # save company details
        self._mailchimp._audience_dict['company'] = self._companyNameEntry.get().strip()
        self._mailchimp._audience_dict['address'] = self._companyAddressEntry.get().strip()
        self._mailchimp._audience_dict['city'] = self._companyCityEntry.get().strip()
        self._mailchimp._audience_dict['state'] = self._companyStateEntry.get().strip()
        self._mailchimp._audience_dict['country'] = self._companyCountryEntry.get().strip()
        self._mailchimp._audience_dict['zip'] = self._companyZipEntry.get().strip()
        self._mailchimp._audience_dict['aud_name'] = self._campaigNameEntry.get().strip() + "_audience"
        self._mailchimp._audience_dict['from_name'] = self._fromNameEntry.get().strip()
        self._mailchimp._audience_dict['from_email'] = self._fromEmailEntry.get().strip()
        self._mailchimp._campaign_dict['subject'] = self._campaignSubjectEntry.get().strip()
        
        with open(f'_companydeets_{self._campaigNameEntry.get().strip()}_.data', 'w') as companydeets:
            companydeets.write("campaign:"+self._campaigNameEntry.get().strip()+"\n")
            companydeets.write("subject:"+self._campaignSubjectEntry.get().strip()+"\n")
            companydeets.write("company:"+self._companyNameEntry.get().strip()+"\n")
            companydeets.write("address:"+self._companyAddressEntry.get().strip()+"\n")
            companydeets.write("city:"+self._companyCityEntry.get().strip()+"\n")
            companydeets.write("state:"+self._companyStateEntry.get().strip()+"\n")
            companydeets.write("country:"+self._companyCountryEntry.get().strip()+"\n")
            companydeets.write("zip:"+self._companyZipEntry.get().strip()+"\n")
            companydeets.write("from_name:"+self._fromNameEntry.get().strip()+"\n")
            companydeets.write("from_email:"+self._fromEmailEntry.get().strip()+"\n")
        
        # clear the fields
        self._campaigNameEntry.delete(0, 'end')
        self._companyNameEntry.delete(0, 'end')
        self._companyAddressEntry.delete(0, 'end')
        self._companyCityEntry.delete(0, 'end')
        self._companyStateEntry.delete(0, 'end')
        self._companyCountryEntry.delete(0, 'end')
        self._companyZipEntry.delete(0, 'end')
        self._campaignSubjectEntry.delete(0, 'end')
        
        self._saveCompanyDetailsCB = False
        
        self._fromEmailEntry.delete(0, 'end')
        self._fromNameEntry.delete(0, 'end')
        
        # export updated campaign list
        self._campaignDataFrame.to_csv('_campaignlist_.csv', index=False)
        self._reinitialize()
        self._menu()
        self._notebook.select(0)

    def _makeCampaignList(self, _EnclosingFrame: ttk.Frame):
        self._CampaignList_control = _list(_EnclosingFrame, self._campaignTreeHeaders, self._campaignTreeData)
    
    def _makeMailingList(self, _EnclosingFrame: ttk.Frame):
        self._mailinglist_control = _list(_EnclosingFrame, self._treeheaders, self._treedata)
    
    def _mailingListAddButton_(self):
        self._userinput()       
    
    def _userinput(self):
        # create a toplevel window
        self._top = Toplevel(self.parent)
        self._top.geometry("500x330+660+350")
        self._top.title(self._title+" -> add mailing info")
        # create enclosing frame
        self._toplevelEnclosingFrame = ttk.Frame(self._top)
        self._toplevelEnclosingFrame.pack(fill=BOTH, expand=True)
        # create form
        self._toplevelFirstFrame = ttk.Frame(self._toplevelEnclosingFrame)
        self._toplevelFirstFrame.pack(fill=BOTH, expand=True)
        self._entername = ttk.Label(self._toplevelFirstFrame, text="Name:")
        self._entername.place(relx=0.34, rely=0.2, anchor='center')
        self._entername_entry = ttk.Entry(self._toplevelFirstFrame, width=15)
        self._entername_entry.place(relx=0.56, rely=0.2, anchor='center')
        self._enteremail = ttk.Label(self._toplevelFirstFrame, text='Email:')
        self._enteremail.place(relx=0.34, rely=0.3, anchor='center')
        self._enteremail_entry = ttk.Entry(self._toplevelFirstFrame, width=15)
        self._enteremail_entry.place(relx=0.56, rely=0.3, anchor='center')
        self._enteraddress = ttk.Label(self._toplevelFirstFrame, text='Address:')
        self._enteraddress.place(relx=0.34, rely=0.4, anchor='center')
        self._enteraddress_entry = ttk.Entry(self._toplevelFirstFrame, width=20)
        self._enteraddress_entry.place(relx=0.61, rely=0.4, anchor='center')
        self._enterphone = ttk.Label(self._toplevelFirstFrame, text='Phone:')
        self._enterphone.place(relx=0.34, rely=0.5, anchor='center')
        self._enterphone_entry = ttk.Entry(self._toplevelFirstFrame, width=15)
        self._enterphone_entry.place(relx=0.56, rely=0.5, anchor='center')
        
        # create submit and back button
        self._toplevelButtonEnclosingFrame = ttk.Frame(self._toplevelEnclosingFrame)
        self._toplevelButtonEnclosingFrame.pack(fill=BOTH)
        self._toplevelSubmitButton = ttk.Button(self._toplevelButtonEnclosingFrame, text='Submit', command=self._toplevelSubmit_)
        self._toplevelSubmitButton.pack(side=LEFT)
        self._toplevelBackButton = ttk.Button(self._toplevelButtonEnclosingFrame, text='back', command=self._toplevelBack_)
        self._toplevelBackButton.pack(side=RIGHT)
        self._top.mainloop()
    
    def _toplevelSubmit_(self):
        ## CANNOT BE EMPTY - FIX IT
        if self._os=='Windows':
            self._dataframe = self._dataframe.append({
                'Serial No.':int(self._dataframe['Serial No.'].count())+1,
                'Name':self._entername_entry.get().strip(),
                'Email':self._enteremail_entry.get().strip(),
                'Address':self._enteraddress_entry.get().strip(),
                'Phone':self._enterphone_entry.get().strip()
            }, ignore_index=True)
        else:
            self._dataframe = self._dataframe._append({
                'Serial No.':int(self._dataframe['Serial No.'].count())+1,
                'Name':self._entername_entry.get().strip(),
                'Email':self._enteremail_entry.get().strip(),
                'Address':self._enteraddress_entry.get().strip(),
                'Phone':self._enterphone_entry.get().strip()
            }, ignore_index=True)
        
        self._top.destroy()
        self._dataframe.to_csv('_mailinglist_.csv', index=False)
        self._reinitialize()
        self._menu()
        self._notebook.select(1)
    
    def _toplevelBack_(self):
        self._top.destroy()

    def _mailingListDeleteButton_(self):
        # create an popup window
        self._topDeleteWindow = Toplevel(self.parent)
        self._topDeleteWindow.title(self._title+" -> Delete Entry")
        self._topDeleteWindow.geometry('300x65+718+490')
        
        # create an enclosing frame
        self._topDeleteWindow_EnclosingFrame = ttk.Frame(self._topDeleteWindow)
        self._topDeleteWindow_EnclosingFrame.pack(fill=BOTH, expand=True)
        
        # create frame for text fields
        self._topDeleteWindow_EnclosingFrame_FirstFrame = ttk.Frame(self._topDeleteWindow_EnclosingFrame)
        self._topDeleteWindow_EnclosingFrame_FirstFrame.pack(fill=BOTH, expand=True)
        
        self._topDeleteWindow_EnterSerialLabel = ttk.Label(self._topDeleteWindow_EnclosingFrame_FirstFrame, text='Serial Number:')
        self._topDeleteWindow_EnterSerialLabel.place(relx=0.3, rely=0.2, anchor="center")
        self._topDeleteWindow_EnterSerialEntry = ttk.Entry(self._topDeleteWindow_EnclosingFrame_FirstFrame, width=8)
        self._topDeleteWindow_EnterSerialEntry.place(relx=0.6, rely=0.2, anchor='center')
        
        # create another frame for buttons
        self._topDeleteWindow_ButtonFrame = ttk.Frame(self._topDeleteWindow_EnclosingFrame)
        self._topDeleteWindow_ButtonFrame.pack(fill=BOTH)
        
        # add buttons
        self._topDeleteWindow_DeleteButton = ttk.Button(self._topDeleteWindow_ButtonFrame, text='delete', command=self._toplevelDelete_)
        self._topDeleteWindow_DeleteButton.pack(side=LEFT)
        self._topDeleteWindow_BackButton = ttk.Button(self._topDeleteWindow_ButtonFrame, text='back', command=self._toplevelBackButton_)
        self._topDeleteWindow_BackButton.pack(side=RIGHT)
        
        self._topDeleteWindow.mainloop()
    
    def _toplevelDelete_(self):
        serial = self._topDeleteWindow_EnterSerialEntry.get().strip()
        self._topDeleteWindow.destroy()
        
        self._dataframe.drop(int(serial)-1, axis=0, inplace=True)
        
        self._dataframe.loc[self._dataframe['Serial No.']>int(serial)-1, 'Serial No.'] -= 1
                        
        self._dataframe.to_csv('_mailinglist_.csv', index=False)
        self._reinitialize()
        self._menu()
        self._notebook.select(1)
    
    def _toplevelBackButton_(self):
        self._topDeleteWindow.destroy()
#!/usr/bin/env python
# #coding=utf-8

#---------------------------------------------------------------------------------

#Compliance with LGPLv3 protocol
#Help Document:https://www.alibabacloud.com/help
#Website:https://www.ghink.net
#Gitee:gitee.com/ghink
#Donate:afdian.net/@ghink

#---------------------------------------------------------------------------------
from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import DescribeDomainsRequest,DescribeDomainRecordsRequest,UpdateDomainRecordRequest
import os
import json
import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DeleteDomainRecordRequest import DeleteDomainRecordRequest
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest

#---------------------------------------------------------------------------------

sets=open('set.json')#Open JSON File
setting = sets.read()#Read JSON File,Sent it in a Variable
sets.close()#Close JSON File

setload = json.loads(setting)#Load JSON
rr = setload['RR']#Save JSON in Variable
domain = setload['Domain']
accesskeyid = setload['accessKeyId']
accesssecret = setload['accessSecret']
ipv4 = setload['IPV4']
ipv6 = setload['IPV6']

#---------------------------------------------------------------------------------

if __name__ == '__main__':
       v4api = 'http://v4.ipv6-test.com/api/myip.php'#Get IPV4 Address
       v4 = requests.get(url=v4api) #IPV4 Address Variable："v4.text"
       print("Your IPV4 Address:")
       print(v4.text)
       v6api = 'http://v6.ip.zxinc.org/getip'#Get IPV6 Address
       v6 = requests.get(url=v6api) #IPV6 Address Variable："v6.text"
       print("Your IPV6 Address:")
       print(v6.text)

#---------------------------------------------------------------------------------

client = AcsClient(accesskeyid, accesssecret, 'cn-hangzhou')#Aliyun AccessKey

#---------------------------------------------------------------------------------

if ipv4 == 'true':#Judging whether IPV4 DDNS is open

    print('Your IPV4 DDNS is open.')

    #Describe IPV4 Records
    describev4 = DescribeDomainRecordsRequest()#Start Describe Domain Records
    describev4.set_accept_format('json')

    describev4.set_DomainName(domain)#Main Domain
    describev4.set_RRKeyWord(rr)#Your RRKeyWord
    describev4.set_TypeKeyWord("A")#Your Record Type

    describebackv4 = client.do_action_with_exception(describev4)#Get Back JSON
    # python2:  print(response) 
    print(str(describebackv4, encoding='utf-8'))#Print JSON

#---------------------------------------------------------------------------------

    #Read IPV4 JSON
    recordlistv4=json.loads(describebackv4)#Read Back JSON
    recordidv4=recordlistv4['DomainRecords']['Record'][0]['RecordId']#Get RecordId From Back JSON
    print('Your IPV4 RecordId：')
    print(recordidv4)
    valuev4=recordlistv4['DomainRecords']['Record'][0]['Value']#Get Value From Back JSON
    print('Your IPV4 Value：')
    print(valuev4)
    #RecordId For IPV4 Variable:"recoredidv4"
    #Value For IPV4 Variable:"valuev4"

#---------------------------------------------------------------------------------

    if valuev4 == v4.text:#Judging whether IPV4 address has changed
        
        #No Change
        print('Your IPV4 Record is Right,Noting to do.')

    else:
        #Changed Already
        print('Your IPV4 Record has Changed,Update Now.')

#---------------------------------------------------------------------------------

    #Update IPV4 Record
    updv4 = UpdateDomainRecordRequest.UpdateDomainRecordRequest()#Start Update Domain Records
    updv4.set_accept_format('json')
    updv4.set_RecordId(recordidv4)
    updv4.set_Value(v4.text)#Set Domain Record From Machine's Internet IPV4 Address
    updv4.set_Type("A")#Set Domain Record Type
    updv4.set_RR(rr)#Set Domain Record RR

    updbackv4 = client.do_action_with_exception(updv4)#Get Back JSON
    # python2:  print(response) 
    print(str(updbackv4, encoding='utf-8'))#Print JSON

#---------------------------------------------------------------------------------

else:
     print('Your have already closed IPV4 DDNS.')

#---------------------------------------------------------------------------------

if ipv6 == "true":#Judging whether IPV6 DDNS is open

    #Describe IPV6 Records
    describev6 = DescribeDomainRecordsRequest()#Start Describe Domain Records
    describev6.set_accept_format('json')

    describev6.set_DomainName(domain)#Main Domain
    describev6.set_RRKeyWord(rr)#Your RRKeyWord
    describev6.set_TypeKeyWord("AAAA")#Your Record Type

    describebackv6 = client.do_action_with_exception(describev6)#Get Back JSON
    # python2:  print(response) 
    print(str(describebackv6, encoding='utf-8'))#Print JSON

#---------------------------------------------------------------------------------

    #Read IPV6 JSON
    recordlistv6=json.loads(describebackv6)#Read Back JSON
    recordidv6=recordlistv6['DomainRecords']['Record'][0]['RecordId']#Get RecordId From Back JSON
    print('Your IPV6 RecordId：')
    print(recordidv6)
    valuev6=recordlistv6['DomainRecords']['Record'][0]['Value']#Get Value From Back JSON
    print('Your IPV6 Value：')
    print(valuev6)
    #RecordId For IPV6 Variable:"recoredidv6"
    #Value For IPV6 Variable:"valuev6"

#---------------------------------------------------------------------------------

    if valuev6 == v6.text:#Judging whether IPV6 address has changed

        #No Change
        print('Your IPV6 Record is Right,Noting to do.')
    
    else:
        #Changed Already
        print('Your IPV6 Record has Changed,Update Now.')

#---------------------------------------------------------------------------------

    #Update IPV6 Record
    #160 line liu
    #updv6 = UpdateDomainRecord()#Start Update Domain Records
    updv6 = UpdateDomainRecordRequest.UpdateDomainRecordRequest()#Start Update Domain Records
    updv6.set_accept_format('json')
    updv6.set_RecordId(recordidv6)
    updv6.set_Value(v6.text)#Set Domain Record From Machine's Internet IPV6 Address
    updv6.set_Type("AAAA")#Set Domain Record Type
    updv6.set_RR(rr)#Set Domain Record RR

    updbackv6 = client.do_action_with_exception(updv6)#Get Back JSON
    # python2:  print(response) 
    print(str(updbackv6, encoding='utf-8'))#Print JSON

#---------------------------------------------------------------------------------

else:
     print('Your have already closed IPV6 DDNS.')

#---------------------------------------------------------------------------------
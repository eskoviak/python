import urllib2

url = 'http://esb2-dev.infarmbureau.com:9081/'

postData = """<IfbiEsbRequest>
                <ClientName>AutoDataPrefill</ClientName>
                <ClientVersion>1.0</ClientVersion>
                <ClientPassword>UpwE6KuTMiJP0VSTg2tv0w==</ClientPassword>
                <ServiceName>Auto-GetPolicyInfo</ServiceName>
                <ServiceVersion>2.b</ServiceVersion>
                <Payload>
                                <Auto-GetPolicyInfoRequest>
                                                <KeyNumber>0008153452</KeyNumber>
                                                <LineOfBusiness>APV</LineOfBusiness>
                                                <EffectiveDate/>
                                                <ExpirationDate/>
                                                <QuoteSeqNumber>0</QuoteSeqNumber>
                                                <BillingRequired>N</BillingRequired>
                                                <PolicyRequired>Y</PolicyRequired>
                                                <ClaimsRequired>N</ClaimsRequired>
                                                <LegacyRequired>N</LegacyRequired>
                                </Auto-GetPolicyInfoRequest>
                </Payload>
</IfbiEsbRequest>
"""

httpHeaders = {
    "Accept": "application/soap+xml,multipart/related,text/*",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Content-Type": "text/xml; charset=utf-8"
}

request = urllib2.Request(url, postData, httpHeaders)

response = urllib2.urlopen(request)

xml_string = response.read()

try:
    outfile = open('autoRs.xml', 'w')
    outfile.write(xml_string)
    outfile.close
except Exception as ex:
    print('Error in file write: ' + ex.message)
    



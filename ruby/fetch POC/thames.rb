require 'HTTMultiParty'

class Thames 
    include HTTMultiParty

    @token = ''

    def self.get_records()
        user = "pablo@aptopayments.com"
        password = "mIl0U4OS4D@WpDxlT!v9rxH#"
        login_url = "https://portal.thamestechnology.co.uk/api/auth"
        response = HTTMultiParty.post(login_url, body: { "Password": password, "EmailAddress": user })
        @token = response.parsed_response
        batch_url = 'https://portal.thamestechnology.co.uk/api/order/batch?page=1&recordsperpage=999999'
        response = HTTMultiParty.get(batch_url, headers: {'Authorization' => "Bearer #{@token}"})
        batch = response.parsed_response
        report_url = "https://portal.thamestechnology.co.uk/api/records?page=1&recordsperpage=999999"
        response = HTTMultiParty.get(report_url, headers: {'Authorization' => "Bearer #{@token}"})
        records = response.parsed_response
        puts(batch)
        puts('######################')
        puts(records)
    end

end

Thames.get_records()


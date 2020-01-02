import urllib.request

test_file_url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
data_from_request = urllib.request.urlopen(test_file_url)

print(data_from_request)
f